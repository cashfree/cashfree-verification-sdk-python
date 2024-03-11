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

class GstinRequestSchema(BaseModel):
    """
    Find the request parameters to verify GSTIN information
    """
    gstin: StrictStr = Field(..., alias="GSTIN", description="It is the unique number assigned to businesses registered under the Goods and Services Tax (GST) system in India.")
    business_name: Optional[StrictStr] = Field('Cashfree', alias="businessName", description="It is the name of the business to which the GSTIN is issued. The maximum character limit is 100.")
    __properties = ["GSTIN", "businessName"]

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
    def from_json(cls, json_str: str) -> GstinRequestSchema:
        """Create an instance of GstinRequestSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> GstinRequestSchema:
        """Create an instance of GstinRequestSchema from a JSON string"""
        temp_dict = json.loads(json_str)
        if "GSTIN, businessName" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> GstinRequestSchema:
        """Create an instance of GstinRequestSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GstinRequestSchema.parse_obj(obj)

        _obj = GstinRequestSchema.parse_obj({
            "gstin": obj.get("GSTIN") if obj.get("GSTIN") is not None else '22AAAAA0000A1Z5',
            "business_name": obj.get("businessName") if obj.get("businessName") is not None else 'Cashfree'
        })
        return _obj

