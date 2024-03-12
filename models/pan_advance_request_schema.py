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

class PanAdvanceRequestSchema(BaseModel):
    """
    Find the request parameters to verify PAN information
    """
    pan: StrictStr = Field(..., description="It is the unique 10-character alphanumeric identifier of the individual issued by the Income Tax Department. The first 5 should be alphabets followed by 4 numbers and the 10th character should again be an alphabet.")
    verification_id: StrictStr = Field(..., description="It is the unique ID you create to identify the verification request. The maximum character limit is 50. Only alphanumeric, period (.), hyphen (-), and underscore ( _ ) are allowed.")
    name: Optional[StrictStr] = Field('JOHN SNOW', description="It is the name of the PAN information holder.")
    __properties = ["pan", "verification_id", "name"]

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
    def from_json(cls, json_str: str) -> PanAdvanceRequestSchema:
        """Create an instance of PanAdvanceRequestSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> PanAdvanceRequestSchema:
        """Create an instance of PanAdvanceRequestSchema from a JSON string"""
        temp_dict = json.loads(json_str)
        if "pan, verification_id, name" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> PanAdvanceRequestSchema:
        """Create an instance of PanAdvanceRequestSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PanAdvanceRequestSchema.parse_obj(obj)

        _obj = PanAdvanceRequestSchema.parse_obj({
            "pan": obj.get("pan") if obj.get("pan") is not None else 'AZJPG7110R',
            "verification_id": obj.get("verification_id") if obj.get("verification_id") is not None else 'testverificationid',
            "name": obj.get("name") if obj.get("name") is not None else 'JOHN SNOW'
        })
        return _obj


