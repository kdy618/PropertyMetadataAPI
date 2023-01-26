# -*- coding: utf-8 -*-
"""Test."""

import pytest
from flask import Response

from hometapapi.repository.model.property_metadata import (
    PropertyMetadataRequest,
    SewerType,
)
from hometapapi.services.third_party_api.house_canary.clients.house_canary_api_client import (
    HouseCanaryAPIClient,
)


class TestHouseCanaryAPIClient:
    @pytest.mark.vcr
    def test_fetch_property_details_with_valid_address(self):
        request = PropertyMetadataRequest("333 N Canal St Apt 2901", "60606")
        client = HouseCanaryAPIClient()
        response = client.fetch_property_details(request)
        assert response.status_code == 200
        assert response.reason == "OK"

    # Recorded the result to cassettes, leverage the file in cassettes to test call out.
    @pytest.mark.vcr
    def test_fetch_property_details_with_invalid_address(self):
        request = PropertyMetadataRequest("33330 N Canal St Apt 2901", "60606")
        client = HouseCanaryAPIClient()
        response = client.fetch_property_details(request)
        assert response.status_code == 403
