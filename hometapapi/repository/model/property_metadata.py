"""Home Metadata Wrapper"""
import re

ZIP_CODE_VALIDATION = re.compile(r'^\d{5}(?:[-\s]\d{4})?$')

class SewerType(Enum):
    MUNICIPAL = "municipal"
    SEPTIC = "septic"
    STORM = "storm"
    
class PropertyMetadata: 
    address = None
    zip_code = None
    has_sewer = None
    sewer = None

class PropertyMetadataRequest:
    address = None
    zip_code = None

    def __init__(self, address, zip_code):
        if ZIP_CODE_VALIDATION.search(zip_code):
            self.zip_code = zip_code
        else:
            raise InvalidAddress()

        #TODO: Add address validation
        self.address = address

