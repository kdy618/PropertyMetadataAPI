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
        # Currently, this method calls HouseCanary API. However, dependening on potential business decisions,
        # we may adjust this function to determine whether it should call HouseCanary API or other APIs or 
        # call another function that contains that decision or etc. 
        return self.house_canary_api.get_property_data(metadata_request)
