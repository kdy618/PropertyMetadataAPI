MUNICIPAL_SEWER = {
            "property/details": {
                "api_code_description": "ok",
                "api_code": 0,
                "result": {
                    "property": {
                        "air_conditioning": "yes",
                        "attic": False,
                        "basement": "full_basement",
                        "building_area_sq_ft": 1824,
                        "building_condition_score": 5,
                        "building_quality_score": 3,
                        "construction_type": "Wood",
                        "exterior_walls": "wood_siding",
                        "fireplace": False,
                        "full_bath_count": 2,
                        "garage_parking_of_cars": 1,
                        "garage_type_parking": "underground_basement",
                        "heating": "forced_air_unit",
                        "heating_fuel_type": "gas",
                        "no_of_buildings": 1,
                        "no_of_stories": 2,
                        "number_of_bedrooms": 4,
                        "number_of_units": 1,
                        "partial_bath_count": 1,
                        "pool": True,
                        "property_type": "Single Family Residential",
                        "roof_cover": "Asphalt",
                        "roof_type": "Wood truss",
                        "site_area_acres": 0.119,
                        "style": "colonial",
                        "total_bath_count": 2.5,
                        "total_number_of_rooms": 7,
                        "sewer": "municipal",
                        "subdivision" : "CITY LAND ASSOCIATION",
                        "water": "municipal",
                        "year_built": 1957,
                        "zoning": "RH1"
                    },

                    "assessment":{
                        "apn": "0000 -1111",
                        "assessment_year": 2015,
                        "tax_year": 2015,
                        "total_assessed_value": 1300000.0,
                        "tax_amount": 15199.86
                    }
                }
            }
        }

SEPTIC_SEWER = {
            "property/details": {
                "api_code_description": "ok",
                "api_code": 0,
                "result": {
                    "property": {
                        "air_conditioning": "yes",
                        "attic": False,
                        "basement": "full_basement",
                        "building_area_sq_ft": 1824,
                        "building_condition_score": 5,
                        "building_quality_score": 3,
                        "construction_type": "Wood",
                        "exterior_walls": "wood_siding",
                        "fireplace": False,
                        "full_bath_count": 2,
                        "garage_parking_of_cars": 1,
                        "garage_type_parking": "underground_basement",
                        "heating": "forced_air_unit",
                        "heating_fuel_type": "gas",
                        "no_of_buildings": 1,
                        "no_of_stories": 2,
                        "number_of_bedrooms": 4,
                        "number_of_units": 1,
                        "partial_bath_count": 1,
                        "pool": True,
                        "property_type": "Single Family Residential",
                        "roof_cover": "Asphalt",
                        "roof_type": "Wood truss",
                        "site_area_acres": 0.119,
                        "style": "colonial",
                        "total_bath_count": 2.5,
                        "total_number_of_rooms": 7,
                        "sewer": "septic",
                        "subdivision" : "CITY LAND ASSOCIATION",
                        "water": "municipal",
                        "year_built": 1957,
                        "zoning": "RH1"
                    },

                    "assessment":{
                        "apn": "0000 -1111",
                        "assessment_year": 2015,
                        "tax_year": 2015,
                        "total_assessed_value": 1300000.0,
                        "tax_amount": 15199.86
                    }
                }
            }
        }

ERROR = {
            "property/details": {
                "api_code_description": "no content",
                "api_code": 204,
                "result": {}
            }
        }

ADDRESS0 = ("320 Summer Street", "02129")
ADDRESS1 = ("420 Autumn Street", "02130")
ADDRESS2 = ("520 Winter Street", "02140")

class MockCanaryAPIClient:
    def get_all_property_metadata(self, address, zip_code):
        if address == ADDRESS0[0] and zip_code == ADDRESS0[1]:
            return MUNICIPAL_SEWER
        
        if address == ADDRESS1[0] and zip_code == ADDRESS1[1]:
            return SEPTIC_SEWER

        return ERROR
