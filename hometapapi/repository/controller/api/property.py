from flask import jsonify

from hometapapi.repository.exceptions import InvalidAddress, RateLimitException
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
                    }
                ),
                200,
            )
        except InvalidAddress:
            # Simple example for surfacing error from API to the controller to view
            # We can add additional message/or info that's consumer friendly
            return (
                jsonify(
                    {
                        "status_code": 403,
                    }
                ),
                403,
            )
        except RateLimitException:
            # Simple example for surfacing error from API to the controller to view
            # We can add additional message/or info that's consumer friendly
            return (
                jsonify(
                    {
                        "status_code": 429,
                    }
                ),
                429,
            )
