
from hometapapi.repository.model.property_metadata import PropertyMetadata, SewerTypes
#from hometapapi.services.api_services.third_party_api.house_canary.clients.mock_canary_api_client import MockCanaryApiClient
from hometapapi.services.property.property_metadata_service import PropertyMetadataService

class HouseCanaryAPIService:
    def __init__(self):
        self.api_client = HouseCanaryAPIClient()

    def get_property_data(self, metadata_request):
        return self._fetch_property_by_api(metadata_request)

    def _fetch_property_by_api(self, metadata_request):
        api_response = self.api_client.fetch_property_details(metadata_request)
        return self._parse_json_data(api_response)

    def _parse_json_data(self, api_response):
        return PropertyMetadata(
            address = api_response.address,
            zip_code = api_response.zip_code,
            sewer = self._parse_sewer_type(api_response.)
            #api_response.get("property/details", {}).get("result", {}).get("property", {}).get("sewer"),
            #has_sewer = self._sewer_check(self.sewer)
        )


    def _parse_sewer_type(self, sewer_data):
        if sewer_data.lower() == "municipal":
            return SewerType.MUNICIPAL
        
        if sewer_data.lower() == "septic":
            return SewerType.SEPTIC

        if sewer_data.lower() == "storm":
            return SewerType.STORM