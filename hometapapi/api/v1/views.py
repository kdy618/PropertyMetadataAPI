# -*- coding: utf-8 -*-
"""API view."""
import logging

from flask import Blueprint, request

from hometapapi.api import api_key_required
from hometapapi.repository.controller.api.property import PropertyAPIController
from hometapapi.services.property.property_metadata_service import (
    PropertyMetadataService,
)
from hometapapi.services.third_party_api.house_canary.clients.house_canary_api_client import (
    HouseCanaryAPIClient,
)

blueprint = Blueprint(
    "api_v1", __name__, url_prefix="/api/v1", static_folder="../static"
)

debug = logging.getLogger()


@blueprint.route("/property/sewer/septic")
@api_key_required
def has_septic_sewer_system():
    """This is the main function to answer the septic system query
    Requires Address & Zipcode
    """
    address = request.args.get("address")
    zip_code = request.args.get("zip_code")
    return PropertyAPIController().has_septic_system(address, zip_code)


@blueprint.route("/property/sewer/septic/debug")
def debug_septic_sewer_system():
    """Use for debugging/troubleshooting"""
    property_service = PropertyMetadataService()
    metadata_request = property_service.create_property_metadata_request(
        "3466 Erie Shore Dr", "48162"
    )
    return HouseCanaryAPIClient().fetch_property_details(metadata_request).json()

@blueprint.route("/property/api/housecanary")
@api_key_required
def view_house_canary_result():
    """Use for viewing full API response object"""

    address = request.args.get("address")
    zip_code = request.args.get("zip_code")
    property_service = PropertyMetadataService()
    metadata_request = property_service.create_property_metadata_request(
        address, zip_code
    )
    return HouseCanaryAPIClient().fetch_property_details(metadata_request).json()
