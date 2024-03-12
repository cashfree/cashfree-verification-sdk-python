# coding: utf-8

"""
    Cashfree Verification API's.

    Cashfree's Verification APIs provide different types of verification to our merchants.

    The version of the OpenAPI document: 2023-12-18
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr

class DrivingLicenseRequestSchema(BaseModel):
    """
    Find the request parameters to retrieve driving licence information
    """
    verification_id: StrictStr = Field(..., description="It is the unique ID you create to identify the verification request. A maximum of 50 characters are allowed. Only alphanumeric, period (.), hyphen (-) and underscore ( _ ) are allowed.")
    dl_number: StrictStr = Field(..., description="It is the driving licence number of the individual for verification.")
    dob: StrictStr = Field(..., description="It is the date of birth of the individual as present in the driving licence. The accepted format is YYYY-MM-DD.")
    __properties = ["verification_id", "dl_number", "dob"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DrivingLicenseRequestSchema:
        """Create an instance of DrivingLicenseRequestSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> DrivingLicenseRequestSchema:
        """Create an instance of DrivingLicenseRequestSchema from a JSON string"""
        temp_dict = json.loads(json_str)
        if "verification_id, dl_number, dob" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DrivingLicenseRequestSchema:
        """Create an instance of DrivingLicenseRequestSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DrivingLicenseRequestSchema.parse_obj(obj)

        _obj = DrivingLicenseRequestSchema.parse_obj({
            "verification_id": obj.get("verification_id") if obj.get("verification_id") is not None else 'test001',
            "dl_number": obj.get("dl_number") if obj.get("dl_number") is not None else 'KA5120190909083',
            "dob": obj.get("dob") if obj.get("dob") is not None else '1993-09-23'
        })
        return _obj

