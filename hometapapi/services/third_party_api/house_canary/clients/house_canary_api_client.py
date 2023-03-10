# -*- coding: utf-8 -*-
"""HouseCanaryAPIClient."""

import housecanary

from hometapapi.settings import HOUSE_CANARY_API_KEY, HOUSE_CANARY_API_SECRET


class HouseCanaryAPIClient:
    def __init__(self):
        self.client = housecanary.ApiClient(
            HOUSE_CANARY_API_KEY, HOUSE_CANARY_API_SECRET
        )

    def fetch_property_details(self, metadata_request):
        # TODO: I'm using test data provided by the test api which does not return any rate info.
        # We should handle rate limit here and determine what the behavior (retry, failing, etc) should be
        # based on business decision.
        response = self.client.property.details(
            (metadata_request.address, metadata_request.zip_code)
        )
        return response
