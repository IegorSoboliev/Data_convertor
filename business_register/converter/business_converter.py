from django.apps import apps

from business_register.models.kved_models import Kved
from data_ocean.models import Authority, Status, TaxpayerType


class BusinessConverter:
    """
    dictionaries whith all kveds, statuses, authorities and taxpayer_types
    """
    all_kveds_dict = {}  
    all_statuses_dict = {}
    all_authorities_dict = {}
    all_taxpayer_types_dict = {}

    def __init__(self):
        """
        initializing dictionaries with all objects from DB
        """
        self.all_kveds_dict = self.put_all_objects_to_dict_with_code("business_register", "Kved")
        self.all_statuses_dict = self.put_all_objects_to_dict_with_name("data_ocean", "Status")
        self.all_authorities_dict = self.put_all_objects_to_dict_with_name("data_ocean", "Authority")
        self.all_taxpayer_types_dict = self.put_all_objects_to_dict_with_name("data_ocean", "TaxpayerType")

    def put_all_objects_to_dict_with_name(self, app_name, model_name):
        """
        putting all objects of the model from DB to a dictionary using name as a key
        """
        model = apps.get_model(app_name, model_name)
        all_objects = model.objects.all()
        all_objects_dict = {}
        for obj in all_objects:
            all_objects_dict[obj.name] = obj
        return all_objects_dict
    
    def put_all_objects_to_dict_with_code(self, app_name, model_name):
        """
        putting all objects of the model from DB to a dictionary using code as a key
        """
        model = apps.get_model(app_name, model_name)
        all_objects = model.objects.all()
        all_objects_dict = {}
        for obj in all_objects:
            all_objects_dict[obj.code]=obj
        return all_objects_dict
        
    def get_kved_from_DB(self, kved_code_from_record):
        """
        retreiving kved from DB or storing the new one
        """
        empty_kved = Kved.objects.get(code='EMP')
        if kved_code_from_record in self.all_kveds_dict:
            return self.all_kveds_dict[kved_code_from_record]
        print(f"This kved value is outdated or not valid")
        return empty_kved
    
    def save_or_get_status(self, status_from_record):
        """
        retreiving status from DB or storing the new one
        """
        if not status_from_record in self.all_statuses_dict:
            new_status = Status(name=status_from_record)
            new_status.save()
            self.all_statuses_dict[status_from_record] = new_status
            return new_status
        return self.all_statuses_dict[status_from_record]

    def save_or_get_authority(self, authority_from_record):
        """
        retreiving authority from DB or storing the new one
        """
        if not authority_from_record in self.all_authorities_dict:
            new_authority = Authority(name=authority_from_record)
            new_authority.save()
            self.all_authorities_dict[authority_from_record] = new_authority
            return new_authority
        return self.all_authorities_dict[authority_from_record]

    def save_or_get_taxpayer_type(self, taxpayer_type_from_record):
        """
        retreiving taxpayer_type from DB or storing the new one
        """
        if not taxpayer_type_from_record in self.all_taxpayer_types_dict:
            new_taxpayer_type = TaxpayerType(name=taxpayer_type_from_record)
            new_taxpayer_type.save()
            self.all_taxpayer_types_dict[taxpayer_type_from_record] = new_taxpayer_type
            return new_taxpayer_type
        return self.all_taxpayer_types_dict[taxpayer_type_from_record]
