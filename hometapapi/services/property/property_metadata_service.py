from hometapapi.services.api_services.house_canary_api_service import HouseCanaryAPIService
from hometapapi.services.property.api_delegate_service import APIDelegateService
from hometapapi.repository.model.property_metadata import PropertyMetadataRequest

class PropertyMetadataService: 
    def __init__(self):
        self.api_delegate = APIDelegateService()

    def create_property_metadata_request(self, address, zip_code):
        return PropertyMetadataRequest(address, zip_code)

    def get_property_data(self, request):
        return self.api_delegate.get_property_data(request)

    def has_septic(self, property_metadata):
        if property_metadata.sewer.lower() == SewerTypes.SEPTIC.value: 
            return True
        else:
            return False

    #def has_windows(): 

    #def has_bedrooms(): 