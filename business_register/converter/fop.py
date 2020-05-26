from django.utils.dateparse import parse_date
from data_ocean.converter import Converter, BulkCreateManager
from business_register.models.rfop_models import Fop, FopToKved, ExchangeDataFop
from data_ocean.models import Status, Authority, TaxpayerType
from django.apps import apps

class FopConverter(Converter):
    bulk_manager = BulkCreateManager()
    all_fops_dict = {}

    def __init__(self):
        all_fops = Fop.objects.all()
        for fop in all_fops:
            self.all_fops_dict[fop.hash_code] = fop

    def save_to_db(self, records):
        for record in records:
            print(record.tag)
            print(record.xpath('NAME')[0].text)
            status = self.save_or_get_status(record.xpath('STAN')[0].text)
            #first getting date, then registration info from one text                
            registration_date = parse_date(self.get_first_word(registration_text))
            registration_info = self.get_other_words(registration_text)
            estate_manager = record.xpath('ESTATE_MANAGER')[0].text
            termination_date = parse_date(self.get_first_word(termination_text))
            terminated_info = self.get_other_words(termination_text)
            termination_cancel_info = record.xpath('TERMINATION_CANCEL_INFO')[0].text
            contact_info = record.xpath('CONTACTS')[0].text
            vp_dates = record.xpath('VP_DATES')[0].text
            authority = self.save_or_get_authority(record.xpath('CURRENT_AUTHORITY')[0].text)
            fullname = record.xpath('NAME')[0].text
            address = record.xpath('ADDRESS')[0].text
            hash_code = hash(fullname + address)
            fop = self.all_fops_dict[hash_code]
            if fop:
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