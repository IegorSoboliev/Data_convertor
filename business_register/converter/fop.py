import datetime

from django.apps import apps

from business_register.models.rfop_models import (ExchangeDataFop, Fop,
                                                  FopToKved)
from data_ocean.converter import BulkCreateManager, Converter
from data_ocean.models import Authority, Status, TaxpayerType


class FopConverter(Converter):
    LOCAL_FILE_NAME = "fop.xml"
    LOCAL_FOLDER = "/Users/marichka/Data_converter/unzipped_xml/"
    DATASET_ID = "1c7f3815-3259-45e0-bdf1-64dca07ddc10"
    CHUNK_SIZE = 5
    bulk_manager = BulkCreateManager(10000)
    all_fops_dict = {}
    all_fop_kveds = []
    all_fop_exchange_data = []

    # def __init__(self):
    all_fops = Fop.objects.all()
    for fop in all_fops:
        all_fops_dict[fop.hash_code] = fop

    def change_date_format(self, date_format):
        datetime.datetime.strptime(date_format, "%d/%m/%Y").strftime("%Y-%m-%d")


    def save_to_db(self, records):
        for record in records:
            print(record.tag)
            print(record.xpath('NAME')[0].text)
            registration_text = record.xpath('REGISTRATION')[0].text
            termination_text = record.xpath('TERMINATED_INFO')[0].text
            status = self.save_or_get_status(record.xpath('STAN')[0].text)
            #first getting date, then registration info if REGISTRATION.text exists
            registration_date = None
            registration_info = None         
            if registration_text:
                print(self.get_first_word(registration_text))
                registration_date = self.format_date_to_yymmdd(self.get_first_word(registration_text))
                registration_info = self.cut_first_word(registration_text)
            estate_manager = record.xpath('ESTATE_MANAGER')[0].text
            termination_date = None
            terminated_info = None         
            if termination_text:
                termination_date = self.format_date_to_yymmdd(self.get_first_word(termination_text))
                terminated_info = self.cut_first_word(termination_text)
            termination_cancel_info = record.xpath('TERMINATION_CANCEL_INFO')[0].text
            contact_info = record.xpath('CONTACTS')[0].text
            vp_dates = record.xpath('VP_DATES')[0].text
            authority = self.save_or_get_authority(record.xpath('CURRENT_AUTHORITY')[0].text)
            fullname = record.xpath('NAME')[0].text
            address = record.xpath('ADDRESS')[0].text
            hash_code = abs(hash(fullname + address)) % (10 ** 9)
            if hash_code in self.all_fops_dict:
                fop = self.all_fops_dict[hash_code]
                fop.status = status
                fop.registration_date = registration_date
                fop.registration_info = registration_info
                fop.estate_manager = estate_manager
                fop.termination_date = termination_date
                fop.terminated_info = terminated_info
                fop.termination_cancel_info = termination_cancel_info
                fop.contact_info = contact_info
                fop.vp_dates = vp_dates
                fop.authority = authority                
            else:
                fop = Fop(
                    hash_code = hash_code,
                    fullname = fullname,
                    address = address,
                    status = status,
                    registration_date = registration_date,
                    registration_info = registration_info,
                    estate_manager = estate_manager,
                    termination_date = termination_date,
                    terminated_info = terminated_info,
                    termination_cancel_info = termination_cancel_info,
                    contact_info = contact_info,
                    vp_dates = vp_dates,
                    authority = authority
                    )
                self.all_fops_dict[hash_code] = fop
            fop_kveds = record.xpath('ACTIVITY_KINDS')[0]
            if len(fop_kveds):
                self.add_fop_kveds_to_list(fop_kveds, hash_code)
            exchange_data = record.xpath('EXCHANGE_DATA')[0]
            if len(exchange_data):
                self.add_exchange_data_to_list(exchange_data, hash_code)
            self.bulk_manager.add(fop)
        self.bulk_manager._commit(Fop)
        self.save_fop_kveds_to_db()
        self.save_exchange_data_to_db()
    
    #putting all kveds into a list
    def add_fop_kveds_to_list(self, fop_kveds, hash_code):
        for activity in fop_kveds:
            info = activity.xpath('ACTIVITY_KIND/CODE')
            if not info:
                return
            kved_code = info[0].text
            kved = self.get_kved_from_DB(kved_code)
            primary = True if activity.xpath('ACTIVITY_KIND/PRIMARY')[0].text == "так" else False
            self.all_fop_kveds.append({"hash_code": hash_code, "kved": kved, "primary": primary})

    #putting all exchange data into a list
    def add_exchange_data_to_list(self, exchange_data, hash_code):
        for answer in exchange_data:
            info = answer.xpath('EXCHANGE_ANSWER/AUTHORITY_NAME')
            if not info:
                return
            authority = self.save_or_get_authority(info[0].text)
            authority.code = answer.xpath('EXCHANGE_ANSWER/AUTHORITY_CODE')[0].text
            #should we use another way to add authority.code?
            authority.save()
            taxpayer_info = answer.xpath('EXCHANGE_ANSWER/TAX_PAYER_TYPE')
            taxpayer_type = None
            if taxpayer_info and taxpayer_info[0].text:
                taxpayer_type = self.save_or_get_taxpayer_type(taxpayer_info[0].text)
            start_date = self.format_date_to_yymmdd(answer.xpath('EXCHANGE_ANSWER/START_DATE')[0].text)
            start_number = answer.xpath('EXCHANGE_ANSWER/START_NUM')[0].text
            end_date = self.format_date_to_yymmdd(answer.xpath('EXCHANGE_ANSWER/END_DATE')[0].text)
            end_number = answer.xpath('EXCHANGE_ANSWER/END_NUM')[0].text
            self.all_fop_exchange_data.append({
                "hash_code": hash_code,
                "authority": authority, 
                "taxpayer_type": taxpayer_type,
                "start_date": start_date,
                "start_number": start_number,
                "end_date": end_date,
                "end_number": end_number
                })

    def save_fop_kveds_to_db(self):
        for dictionary in self.all_fop_kveds:
            fop_to_kved = FopToKved()
            #Is there a way not to get to DB every time?
            fop_to_kved.fop = Fop.objects.get(hash_code=dictionary["hash_code"])
            fop_to_kved.kved = dictionary["kved"]
            fop_to_kved.primary_kved = dictionary["primary"]
            self.bulk_manager.add(fop_to_kved)
        self.bulk_manager._commit(FopToKved)
    
    def save_exchange_data_to_db(self):
        for dictionary in self.all_fop_exchange_data:
            exchange_data = ExchangeDataFop()
            #Is there a way not to get to DB every time?
            exchange_data.fop = Fop.objects.get(hash_code=dictionary["hash_code"])
            exchange_data.authority = dictionary["authority"]
            exchange_data.taxpayer_type = dictionary["taxpayer_type"]
            exchange_data.start_date = dictionary["start_date"]
            exchange_data.start_number = dictionary["start_number"]
            exchange_data.end_date = dictionary["end_date"]
            exchange_data.end_number = dictionary["end_number"]
            self.bulk_manager.add(exchange_data)
        self.bulk_manager._commit(ExchangeDataFop)
        
    print("For storing run FopConverter().process_full()")