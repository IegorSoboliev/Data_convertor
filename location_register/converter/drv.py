# Drv means 'Державний реєстр виборців' - the source for addresses data
import re
from zeep import Client, Settings
from zeep.helpers import serialize_object
from data_ocean.converter import Converter
from location_register.models.drv_models import DrvRegion, DrvDistrict, DrvCouncil, DrvAto, DrvStreet, ZipCode, DrvBuilding

class DrvConverter(Converter):
    WSDL_URL = 'https://www.drv.gov.ua/ords/svc/personal/API/Opendata'
    SETTINGS = Settings(strict=False, xml_huge_tree=True)

    all_regions_dict = {}

    # changing from records like: "с.високе" to "високе", "м.судак" to "судак", "смт.научне" to "научне", "сщ.стальне" to "стальне", "с/рада.вілінська" to "вілінська", "сщ/рада.поштівська" to "поштівська"
    def clean_name(self, name):
        return re.sub(r"с\.|м\.|смт\.|сщ\.|с/рада\.|сщ/рада\.|р\.", "", name).strip()

    def parse_regions_data(self):
        client = Client(self.WSDL_URL, service_name='GetRegionsService', settings=self.SETTINGS)
        response = client.service.GetRegions()
        # converting zeep object to Python ordered dictionary
        response_to_dict = serialize_object(response)
        # accessing a nested list with regions data as dictionaries
        return response_to_dict['Region']

    def save_to_region_table(self, regions_dictionaries):
        self.all_regions_dict = self.initialize_objects_for('location_register', 'DrvRegion')
        for dictionary in regions_dictionaries:
            code = dictionary['Region_Id']
            number = dictionary['Region_Num']
            name = dictionary['Region_Name']
            # deleting 'м. ' from records like 'м. Київ'
            name = self.clean_name(name)
            short_name = dictionary['Region_Short']
            capital = dictionary['Region_Center']
            if capital:
                # deleting 'м. ' from records like 'м. Київ'
                capital = self.clean_name(capital)
            if name in self.all_regions_dict:
                region = self.all_regions_dict[name]
                region.code = code
                region.number = number
                region.short_name = short_name
                region.capital = capital
            else:
                region = DrvRegion(code=code, number=number, name=name, short_name=short_name, capital=capital)
                self.all_regions_dict[name] = region
            region.save()
    
    def parse_Ato_data(self):
        client = Client(self.WSDL_URL, service_name='GetRegionsService', settings=self.SETTINGS)
        response = client.service.GetRegions()
        # converting zeep object to Python ordered dictionary
        response_to_dict = serialize_object(response)
        # accessing a nested list with regions data as dictionaries
        return response_to_dict['Region']

    def process(self):
        regions_dictionaries = self.parse_regions_data()
        self.save_to_region_table(regions_dictionaries)

DrvConverter().process()