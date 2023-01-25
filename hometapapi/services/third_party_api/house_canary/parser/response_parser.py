from flask import current_app

from hometapapi.repository.model.property_metadata import PropertyMetadata, SewerType


class HouseCanaryResponseParser:
    # Assuming json response object only returns 1 object in the list
    def parse_property_details(self, api_response):
        current_app.logger.warn(api_response)
        return PropertyMetadata(
            address=self._get_address(api_response[0]),
            zip_code=self._get_zip_code(api_response[0]),
            sewer=self._get_sewer(api_response[0]),
        )

    def _get_sewer(self, api_response):
        sewer = (
            api_response.get("property/details", {})
            .get("result", {})
            .get("property", {})
            .get("sewer")
        )
        return self._parse_sewer_type(sewer)

    def _get_address(self, api_response):
        return api_response.get("address_info", {}).get("address")

    def _get_zip_code(self, api_response):
        return api_response.get("address_info", {}).get("zipcode")

    def _parse_sewer_type(self, sewer_data):
        if sewer_data == None:
            return SewerType.NONE

        if sewer_data.lower() == "municipal":
            return SewerType.MUNICIPAL

        if sewer_data.lower() == "septic":
            return SewerType.SEPTIC

        if sewer_data.lower() == "storm":
            return SewerType.STORM

        if sewer_data.lower() == "yes":
            return SewerType.YES
