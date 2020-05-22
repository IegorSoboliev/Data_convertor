from django.utils.dateparse import parse_date
from data_ocean.converter import Converter, BulkCreateManager
from business_register.models.rfop_models import Fop, FopToKved, ExchangeDataFop
from data_ocean.models import Status, Authority, TaxpayerType
from django.apps import apps

class FopConverter(Converter):
    bulk_manager = BulkCreateManager()

    def save_to_db(self, records):
        for record in records:
            print(record.tag)
            print(record.xpath('NAME')[0].text)
            registration_text = record.xpath('REGISTRATION')[0].text
            termination_text = record.xpath('TERMINATED_INFO')[0].text
            fop = Fop(
                fullname = record.xpath('NAME')[0].text,
                address = record.xpath('ADDRESS')[0].text,
                status = self.get_or_save_to_DB(record.xpath('STAN')[0].text, Status),
                #first getting date, then registration info from one text                
                registration_date = parse_date(self.get_first_word(registration_text)),
                registration_info = self.get_other_words(registration_text),
                estate_manager = record.xpath('ESTATE_MANAGER')[0].text,
                termination_date = parse_date(self.get_first_word(termination_text)),
                terminated_info = self.get_other_words(termination_text),
                termination_cancel_info = record.xpath('TERMINATION_CANCEL_INFO')[0].text,
                contact_info = record.xpath('CONTACTS')[0].text,
                vp_dates = record.xpath('VP_DATES')[0].text,
                authority = self.get_or_save_to_DB(record.xpath('CURRENT_AUTHORITY')[0].text, Authority)
                )
            self.bulk_manager.add(fop)
        self.bulk_manager._commit(Fop)