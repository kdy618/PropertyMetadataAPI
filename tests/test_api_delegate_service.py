import pytest

from hometapapi.repository.model.property_metadata import (
    PropertyMetadataRequest,
    SewerType,
)
from hometapapi.services.property.api_delegate_service import APIDelegateService
from hometapapi.services.third_party_api.house_canary.house_canary_api_service import (
    HouseCanaryAPIService,
)


class TestAPIDelegateService:
    def test_delegates_to_house_canary(self):
        api_delegate = APIDelegateService()
        assert isinstance(api_delegate.house_canary_api, HouseCanaryAPIService)

    @pytest.mark.vcr
    def test_get_property_data(self):
        api_delegate = APIDelegateService()
        request = PropertyMetadataRequest("333 N Canal St Apt 2901", "60606")
        property_metadata = api_delegate.get_property_data(request)
        assert property_metadata.address == "333 N Canal St"
        assert property_metadata.zip_code == "60606"
        assert property_metadata.sewer == SewerType.NONE
