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

class VpaFromPhone500Schema(BaseModel):
    """
    Internal error response
    """
    status: Optional[StrictStr] = Field(None, description="It displays the status of the API request.")
    verification_id: Optional[StrictStr] = Field(None, description="It displays the unique ID you created to identify the API request.")
    message: Optional[StrictStr] = Field(None, description="It displays details about the success or failure of the API request")
    reference_id: Optional[StrictInt] = Field(None, description="It displays the unique ID created by Cashfree Payments for reference purposes.")
    account_status: Optional[StrictStr] = Field(None, description="It displays the status of the account.")
    mobile_number: Optional[StrictStr] = Field(None, description="It displays the mobile number of the individual.")
    __properties = ["status", "verification_id", "message", "reference_id", "account_status", "mobile_number"]

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
    def from_json(cls, json_str: str) -> VpaFromPhone500Schema:
        """Create an instance of VpaFromPhone500Schema from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> VpaFromPhone500Schema:
        """Create an instance of VpaFromPhone500Schema from a JSON string"""
        temp_dict = json.loads(json_str)
        if "status, verification_id, message, reference_id, account_status, mobile_number" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> VpaFromPhone500Schema:
        """Create an instance of VpaFromPhone500Schema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VpaFromPhone500Schema.parse_obj(obj)

        _obj = VpaFromPhone500Schema.parse_obj({
            "status": obj.get("status"),
            "verification_id": obj.get("verification_id"),
            "message": obj.get("message"),
            "reference_id": obj.get("reference_id"),
            "account_status": obj.get("account_status"),
            "mobile_number": obj.get("mobile_number")
        })
        return _obj


