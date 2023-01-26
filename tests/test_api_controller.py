import pytest

from hometapapi.repository.controller.api.property import PropertyAPIController
from hometapapi.services.property.property_metadata_service import (
    PropertyMetadataService,
)


class TestAPIController:
    @pytest.mark.vcr
    def test_has_septic_valid(self):
        address = "333 N Canal St Apt 2901"
        zip_code = "60606"
        response = PropertyAPIController().has_septic_system(address, zip_code)
        assert response[0].json["has_septic"] == False
        assert response[0].status_code == 200

    @pytest.mark.vcr
    def test_has_septic_invalid_address(self):
        address = ""
        zip_code = "60606"
        rez = PropertyAPIController().has_septic_system(address, zip_code)
        assert rez[1] == 400
