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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class UpiMobileResponseSchema(BaseModel):
    """
    Success response
    """
    reference_id: Optional[StrictInt] = Field(None, description="It displays the unique ID created by Cashfree Payments for reference purposes.")
    status: Optional[StrictStr] = Field(None, description="It displays the status of the API request.")
    account_status: Optional[StrictStr] = Field(None, description="It displays the status of the UPI VPA information.")
    verification_id: Optional[StrictStr] = Field(None, description="It displays the unique ID you created to identify the verification request.")
    mobile_number: Optional[StrictStr] = Field(None, description="It displays the mobile number of the account holder.")
    vpa: Optional[StrictStr] = Field(None, description="It displays the UPI VPA associated with the entered mobile number. If no primary UPI VPA is associated, tis field will be null.")
    name_at_bank: Optional[StrictStr] = Field(None, description="It displays the name of the account holder as registered in the bank. If no primary UPI VPA is associated, this field will be null.")
    additional_vpas: Optional[conlist(StrictStr)] = Field(None, description="It displays the list of additional UPI VPA associated with the mobile number. If no other UPI VPA is linked with the mobile number, this will be an empty array [].")
    __properties = ["reference_id", "status", "account_status", "verification_id", "mobile_number", "vpa", "name_at_bank", "additional_vpas"]

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
    def from_json(cls, json_str: str) -> UpiMobileResponseSchema:
        """Create an instance of UpiMobileResponseSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> UpiMobileResponseSchema:
        """Create an instance of UpiMobileResponseSchema from a JSON string"""
        temp_dict = json.loads(json_str)
        if "reference_id, status, account_status, verification_id, mobile_number, vpa, name_at_bank, additional_vpas" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> UpiMobileResponseSchema:
        """Create an instance of UpiMobileResponseSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpiMobileResponseSchema.parse_obj(obj)

        _obj = UpiMobileResponseSchema.parse_obj({
            "reference_id": obj.get("reference_id"),
            "status": obj.get("status"),
            "account_status": obj.get("account_status"),
            "verification_id": obj.get("verification_id"),
            "mobile_number": obj.get("mobile_number"),
            "vpa": obj.get("vpa"),
            "name_at_bank": obj.get("name_at_bank"),
            "additional_vpas": obj.get("additional_vpas")
        })
        return _obj


