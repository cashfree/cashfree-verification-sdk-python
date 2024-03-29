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
from pydantic import BaseModel, Field, StrictStr

class UpiAdvanceRequestSchema(BaseModel):
    """
    Find the request parameters to verify UPI VPA information
    """
    vpa: StrictStr = Field(..., description="It is the UPI VPA information. Only alphanumeric characters with period (.), hyphen (-), and underscore ( _ ), at the rate of (@) are allowed.")
    name: Optional[StrictStr] = Field('John Doe', description="It is the name of the UPI VPA account holder.")
    __properties = ["vpa", "name"]

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
    def from_json(cls, json_str: str) -> UpiAdvanceRequestSchema:
        """Create an instance of UpiAdvanceRequestSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> UpiAdvanceRequestSchema:
        """Create an instance of UpiAdvanceRequestSchema from a JSON string"""
        temp_dict = json.loads(json_str)
        if "vpa, name" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> UpiAdvanceRequestSchema:
        """Create an instance of UpiAdvanceRequestSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpiAdvanceRequestSchema.parse_obj(obj)

        _obj = UpiAdvanceRequestSchema.parse_obj({
            "vpa": obj.get("vpa") if obj.get("vpa") is not None else 'valid_vpa@upi',
            "name": obj.get("name") if obj.get("name") is not None else 'John Doe'
        })
        return _obj


