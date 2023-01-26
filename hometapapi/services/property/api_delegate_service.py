# -*- coding: utf-8 -*-
"""API Delegate Service, which passes data between PropertyMetadataService and
the APIServices/Clients. 

Future APIs will interface at this point to combine data or determine correct
API to call.
"""

from hometapapi.services.third_party_api.house_canary.house_canary_api_service import (
    HouseCanaryAPIService,
)


class APIDelegateService:
    def __init__(self):
        self.house_canary_api = HouseCanaryAPIService()

    def get_property_data(self, metadata_request):
        return self.house_canary_api.get_property_data(metadata_request)
