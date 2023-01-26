# -*- coding: utf-8 -*-
"""Controller."""

from flask import jsonify

from hometapapi.repository.exceptions import (
    AuthenticationException,
    InvalidAddress,
    MissingRequiredParamException,
    RateLimitException,
)
from hometapapi.services.property.property_metadata_service import (
    PropertyMetadataService,
)
from hometapapi.services.third_party_api.house_canary.clients.house_canary_api_client import (
    HouseCanaryAPIClient,
)


class PropertyAPIController:
    def has_septic_system(self, address, zip_code):
        property_service = PropertyMetadataService()
        try:
            metadata_request = property_service.create_property_metadata_request(
                address, zip_code
            )
            property_metadata = property_service.get_property_data(metadata_request)
            return (
                jsonify(
                    {
                        "has_septic": property_service.has_septic(property_metadata),
                        "status_code": 200,
                        "message": "Request succeeded"
                    }
                ),
                200,
            )
        except InvalidAddress:
            return (
                jsonify(
                    {
                        "status_code": 403,
                        "message": "Invalid or unsupported address",

                    }
                ),
                400,
            )
        except RateLimitException:
            return (
                jsonify(
                    {
                        "status_code": 429,
                        "message": "Rate limit exceeded",
                    }
                ),
                429,
            )
        except AuthenticationException:
            return (
                jsonify(
                    {
                        "status_code": 401,
                        "message": "Authentication issue",
                    }
                ),
                401,
            )
        except MissingRequiredParamException:
            return (
                jsonify(
                    {
                        "status_code": 400,
                        "message": "Missing parameters",
                    }
                ),
                400,
            )
