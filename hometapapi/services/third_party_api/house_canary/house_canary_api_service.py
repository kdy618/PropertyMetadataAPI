# -*- coding: utf-8 -*-
"""HouseCanaryAPIService."""

from hometapapi.repository.exceptions import (
    AuthenticationException,
    InvalidAddress,
    MissingRequiredParamException,
    RateLimitException,
)
from hometapapi.repository.model.property_metadata import PropertyMetadata, SewerType
from hometapapi.services.third_party_api.house_canary.clients.house_canary_api_client import (
    HouseCanaryAPIClient,
)
from hometapapi.services.third_party_api.house_canary.parser.response_parser import (
    HouseCanaryResponseParser,
)


class HouseCanaryAPIService:
    def __init__(self):
        self.api_client = HouseCanaryAPIClient()

    def get_property_data(self, metadata_request):
        return self._fetch_property_by_api(metadata_request)

    def _fetch_property_by_api(self, metadata_request):
        api_response = self.api_client.fetch_property_details(metadata_request)
        if api_response.status_code == 403:
            raise InvalidAddress()
        if api_response.status_code == 429:
            raise RateLimitException()
        if api_response.status_code == 400:
            raise MissingRequiredParamException()
        if api_response.status_code == 401:
            raise AuthenticationException()
        return self._get_property_metadata(api_response.json())

    def _get_property_metadata(self, api_response):
        return HouseCanaryResponseParser().parse_property_details(api_response)
