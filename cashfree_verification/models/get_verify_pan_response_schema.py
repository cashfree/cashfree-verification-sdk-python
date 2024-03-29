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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class GetVerifyPanResponseSchema(BaseModel):
    """
    Success response for Verify PAN Sync API
    """
    pan: Optional[StrictStr] = Field(None, description="It displays the unique 10-character alphanumeric identifier issued by the Income Tax Department.")
    type: Optional[StrictStr] = Field(None, description="It displays the type of the PAN issued.")
    reference_id: Optional[StrictInt] = Field(None, description="It displays the unique ID created by Cashfree Payments for reference purposes.")
    name_provided: Optional[StrictStr] = Field(None, description="It displays the name entered in the API request.")
    registered_name: Optional[StrictStr] = Field(None, description="It displays the PAN registered name.")
    valid: Optional[StrictBool] = Field(None, description="It displays the status of the PAN card.")
    father_name: Optional[StrictStr] = Field(None, description="It displays the father's name of the PAN card holder.")
    message: Optional[StrictStr] = Field(None, description="It displays details about the success or failure of the API request.")
    name_match_score: Optional[StrictStr] = Field(None, description="It displays the score for the name match verification.")
    name_match_result: Optional[StrictStr] = Field(None, description="It displays the result of the name match verification.")
    aadhaar_seeding_status: Optional[StrictStr] = Field(None, description="It displays whether the individual linked the aadhaar information with PAN.")
    last_updated_at: Optional[StrictStr] = Field(None, description="It displays the last updated date.")
    name_pan_card: Optional[StrictStr] = Field(None, description="It displays the name displayed on the PAN card.")
    pan_status: Optional[StrictStr] = Field(None, description="It displays the status of the PAN card.")
    aadhaar_seeding_status_desc: Optional[StrictStr] = Field(None, description="It displays additional information of the linking of aadhaar and PAN card.")
    __properties = ["pan", "type", "reference_id", "name_provided", "registered_name", "valid", "father_name", "message", "name_match_score", "name_match_result", "aadhaar_seeding_status", "last_updated_at", "name_pan_card", "pan_status", "aadhaar_seeding_status_desc"]

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
    def from_json(cls, json_str: str) -> GetVerifyPanResponseSchema:
        """Create an instance of GetVerifyPanResponseSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> GetVerifyPanResponseSchema:
        """Create an instance of GetVerifyPanResponseSchema from a JSON string"""
        temp_dict = json.loads(json_str)
        if "pan, type, reference_id, name_provided, registered_name, valid, father_name, message, name_match_score, name_match_result, aadhaar_seeding_status, last_updated_at, name_pan_card, pan_status, aadhaar_seeding_status_desc" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> GetVerifyPanResponseSchema:
        """Create an instance of GetVerifyPanResponseSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetVerifyPanResponseSchema.parse_obj(obj)

        _obj = GetVerifyPanResponseSchema.parse_obj({
            "pan": obj.get("pan"),
            "type": obj.get("type"),
            "reference_id": obj.get("reference_id"),
            "name_provided": obj.get("name_provided"),
            "registered_name": obj.get("registered_name"),
            "valid": obj.get("valid"),
            "father_name": obj.get("father_name"),
            "message": obj.get("message"),
            "name_match_score": obj.get("name_match_score"),
            "name_match_result": obj.get("name_match_result"),
            "aadhaar_seeding_status": obj.get("aadhaar_seeding_status"),
            "last_updated_at": obj.get("last_updated_at"),
            "name_pan_card": obj.get("name_pan_card"),
            "pan_status": obj.get("pan_status"),
            "aadhaar_seeding_status_desc": obj.get("aadhaar_seeding_status_desc")
        })
        return _obj


