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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class AadhaarMaskingResponseSchema(BaseModel):
    """
    Success response for Aadhaar Masking API
    """
    status: Optional[StrictStr] = Field(None, description="It displays the status of the aadhaar information.")
    reference_id: Optional[StrictInt] = Field(None, description="It displays the unique ID created by Cashfree Payments for reference purposes.")
    verification_id: Optional[StrictStr] = Field(None, description="It displays the unique ID you created to identify the verification request")
    image_link: Optional[StrictStr] = Field(None, description="It displays the URL of the image.")
    __properties = ["status", "reference_id", "verification_id", "image_link"]

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
    def from_json(cls, json_str: str) -> AadhaarMaskingResponseSchema:
        """Create an instance of AadhaarMaskingResponseSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> AadhaarMaskingResponseSchema:
        """Create an instance of AadhaarMaskingResponseSchema from a JSON string"""
        temp_dict = json.loads(json_str)
        if "status, reference_id, verification_id, image_link" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> AadhaarMaskingResponseSchema:
        """Create an instance of AadhaarMaskingResponseSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AadhaarMaskingResponseSchema.parse_obj(obj)

        _obj = AadhaarMaskingResponseSchema.parse_obj({
            "status": obj.get("status"),
            "reference_id": obj.get("reference_id"),
            "verification_id": obj.get("verification_id"),
            "image_link": obj.get("image_link")
        })
        return _obj

