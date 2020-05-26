from django.utils.dateparse import parse_date
from data_ocean.converter import Converter, BulkCreateManager
from business_register.models.rfop_models import Fop, FopToKved, ExchangeDataFop
from data_ocean.models import Status, Authority, TaxpayerType
from django.apps import apps

class FopConverter(Converter):
    LOCAL_FILE_NAME = "fop.xml"
    LOCAL_FOLDER = "/Users/marichka/Data_converter/unzipped_xml/"
    DATASET_ID = "1c7f3815-3259-45e0-bdf1-64dca07ddc10"
    CHUNK_SIZE = 5
    bulk_manager = BulkCreateManager(10000)
    all_fops_dict = {}

    def __init__(self):
        all_fops = Fop.objects.all()
        for fop in all_fops:
            self.all_fops_dict[fop.hash_code] = fop

    def save_to_db(self, records):
        for record in records:
            print(record.tag)
            print(record.xpath('NAME')[0].text)
            registration_text = record.xpath('REGISTRATION')[0].text
            termination_text = record.xpath('TERMINATED_INFO')[0].text
            status = self.save_or_get_status(record.xpath('STAN')[0].text)
            #first getting date, then registration info from one text                
            registration_date = parse_date(self.get_first_word(registration_text))
            registration_info = self.cut_first_word(registration_text)
            estate_manager = record.xpath('ESTATE_MANAGER')[0].text
            termination_date = parse_date(self.get_first_word(termination_text))
            terminated_info = self.cut_first_word(termination_text)
            termination_cancel_info = record.xpath('TERMINATION_CANCEL_INFO')[0].text
            contact_info = record.xpath('CONTACTS')[0].text
            vp_dates = record.xpath('VP_DATES')[0].text
            authority = self.save_or_get_authority(record.xpath('CURRENT_AUTHORITY')[0].text)
            fullname = record.xpath('NAME')[0].text
            address = record.xpath('ADDRESS')[0].text
            hash_code = hash(fullname + address)
            if hash_code in self.all_fops_dict:
                fop = self.all_fops_dict[hash_code]
                fop.status = status
                #first getting date, then registration info from one text                
                fop.registration_date = registration_date
                fop.registration_info = registration_info
                fop.estate_manager = estate_manager
                fop.termination_date = termination_date
                fop.terminated_info = terminated_info
                fop.termination_cancel_info = termination_cancel_info
                fop.contact_info = contact_info
                fop.vp_dates = vp_dates
                fop.authority = authority                
                self.bulk_manager.add(fop)
            self.bulk_manager._commit(Fop)
            fop = Fop(
                hash_code = hash_code,
                fullname = fullname,
                address = address,
                status = status,
                #first getting date, then registration info from one text                
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
            self.bulk_manager.add(fop)
        self.bulk_manager._commit(Fop)
        #adding other fields for saved object
        index = 0    
        for record in records:
            fop = self.bulk_manager._create_queues['business_register.Fop'][index]
            for kind in record.xpath('ACTIVITY_KINDS'):
                fop_to_kved = FopToKved()
                fop_to_kved.kved = self.get_kved_from_DB(kind.xpath('CODE')[0].text)
                if kind.xpath('PRIMARY')[0].text == "так": 
                    fop_to_kved.primary_kved = True
                fop_to_kved.fop = fop
                self.bulk_manager.add(fop_to_kved)
            for answer in record.xpath('EXCHANGE_DATA'):
                exchange_data = ExchangeDataFop()
                exchange_data.start_date = parse_date(answer.xpath('START_DATE')[0].text)
                exchange_data.start_number = answer.xpath('START_NUM')[0].text
                exchange_data.end_date = parse_date(answer.xpath('END_DATE')[0].text)
                exchange_data.end_number = answer.xpath('END_NUM')[0].text
                authority = self.save_or_get_authority(answer.xpath('AUTHORITY_NAME')[0].text)
                authority.code = answer.xpath('AUTHORITY_CODE')[0].text
                #should we add defaults here?
                authority.save()
                exchange_data.authority = authority
                exchange_data.fop = fop
                exchange_data.taxpayer_type = answer.xpath('TAX_PAYER_TYPE')[0].text
                self.bulk_manager.add(exchange_data)
            index = index + 1
        self.bulk_manager._commit(FopToKved)
        self.bulk_manager._commit(ExchangeDataFop)
