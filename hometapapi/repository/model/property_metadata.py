"""Home Metadata Wrapper"""
import re
from enum import Enum

ZIP_CODE_VALIDATION = re.compile(r"^\d{5}(?:[-\s]\d{4})?$")


class SewerType(Enum):
    MUNICIPAL = "municipal"
    SEPTIC = "septic"
    STORM = "storm"
    NONE = "none"
    YES = "yes"


class PropertyMetadata:
    address = None
    zip_code = None
    sewer = None

    def __init__(self, address, zip_code, sewer):
        self.address = address
        self.zip_code = zip_code
        self.sewer = sewer


class PropertyMetadataRequest:
    address = None
    zip_code = None

    def __init__(self, address, zip_code):
        if ZIP_CODE_VALIDATION.search(zip_code):
            self.zip_code = zip_code
        else:
            raise InvalidAddress()

        # TODO: Add address validation
        self.address = address
