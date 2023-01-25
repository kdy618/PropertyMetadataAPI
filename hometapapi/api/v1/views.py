# -*- coding: utf-8 -*-
"""API views."""
from flask import Blueprint, render_template
from flask_login import login_required

from hometapapi.services.property.property_metadata_service import PropertyMetadataService

blueprint = Blueprint("api_v1", __name__, url_prefix="/api/v1", static_folder="../static")


@blueprint.route("/property/sewer/septic")
@login_required
def has_septic_sewer_system():
    property_service = PropertyMetadataService()
    metadata_request = property_service.create_property_metadata_request(address, zip_code)
    property_metadata = property_service.get_property_data(metadata_request)
    
    return house_service.get_all_metadata(None, None)
