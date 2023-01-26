# -*- coding: utf-8 -*-
"""Test."""

import pytest

from hometapapi.repository.exceptions import (
    AuthenticationException,
    InvalidAddress,
    MissingRequiredParamException,
    RateLimitException,
)
from hometapapi.repository.model.property_metadata import (
    PropertyMetadataRequest,
    SewerType,
)
from hometapapi.services.third_party_api.house_canary.clients.house_canary_api_client import (
    HouseCanaryAPIClient,
)
from hometapapi.services.third_party_api.house_canary.house_canary_api_service import (
    HouseCanaryAPIService,
)


class MockResponse:
    status_code = None

    def __init__(self, status_code):
        self.status_code = status_code


class MonkeyPatchErrorAPIClient:
    def __init__(self, status_code):
        self.status_code = status_code

    def fetch_property_details(self, metadata_request):
        return MockResponse(self.status_code)


class TestHouseCanaryAPIService:
    @pytest.mark.vcr
    def test_fetch_property_details_with_valid_address(self):
        request = PropertyMetadataRequest("333 N Canal St Apt 2901", "60606")
        service = HouseCanaryAPIService()
        property_metadata = service.get_property_data(request)
        assert property_metadata.address == "333 N Canal St"
        assert property_metadata.zip_code == "60606"
        assert property_metadata.sewer == SewerType.NONE

    # Recorded the result to the cassettes, leverage the file in cassette to test exceptions.
    @pytest.mark.vcr
    def test_fetch_property_details_with_rate_limit(self):
        with pytest.raises(InvalidAddress):
            request = PropertyMetadataRequest("30293 N Canal St Apt 2901", "60606")
            service = HouseCanaryAPIService()
            service.api_client = MonkeyPatchErrorAPIClient(403)
            response = service.get_property_data(request)
            assert response.status_code == 403

    @pytest.mark.vcr
    def test_fetch_property_details_with_rate_limit(self):
        with pytest.raises(RateLimitException):
            request = PropertyMetadataRequest("333 N Canal St Apt 2901", "60606")
            service = HouseCanaryAPIService()
            service.api_client = MonkeyPatchErrorAPIClient(429)
            response = service.get_property_data(request)
            assert response.status_code == 429

    @pytest.mark.vcr
    def test_fetch_property_details_with_authentication_issue(self):
        with pytest.raises(AuthenticationException):
            request = PropertyMetadataRequest("333 N Canal St Apt 2901", "60606")
            service = HouseCanaryAPIService()
            service.api_client = MonkeyPatchErrorAPIClient(401)
            response = service.get_property_data(request)
            assert response.status_code == 401

    @pytest.mark.vcr
    def test_fetch_property_details_with_missing_param(self):
        with pytest.raises(MissingRequiredParamException):
            request = PropertyMetadataRequest("", "60606")
            service = HouseCanaryAPIService()
            service.api_client = MonkeyPatchErrorAPIClient(400)
            response = service.get_property_data(request)
            assert response.status_code == 400
