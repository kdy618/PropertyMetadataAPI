from hometapapi.services.third_party_api.house_canary.house_canary_api_service import HouseCanaryAPIService


class APIDelegateService:
    def __init__(self):
        self.house_canary_api = HouseCanaryAPIService()

    def get_property_data(metadata_request):
        return self.house_canary_api.get_property_data(metadata_request)