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

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field
from cashfree_verification.models.validity_details import ValidityDetails

class DrivingLicenseResponseSchemaDlValidity(BaseModel):
    """
    It contains the different information regarding the validity of the licence.
    """
    non_transport: Optional[ValidityDetails] = None
    hazardous_valid_till: Optional[date] = Field(None, description="It displays till when the individual can drive hazardous vehicle.")
    transport: Optional[ValidityDetails] = None
    hill_valid_till: Optional[date] = Field(None, description="It displays till when the individual can drive the vehicle in hill and mountain regions.")
    __properties = ["non_transport", "hazardous_valid_till", "transport", "hill_valid_till"]

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
    def from_json(cls, json_str: str) -> DrivingLicenseResponseSchemaDlValidity:
        """Create an instance of DrivingLicenseResponseSchemaDlValidity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> DrivingLicenseResponseSchemaDlValidity:
        """Create an instance of DrivingLicenseResponseSchemaDlValidity from a JSON string"""
        temp_dict = json.loads(json_str)
        if "non_transport, hazardous_valid_till, transport, hill_valid_till" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of non_transport
        if self.non_transport:
            _dict['non_transport'] = self.non_transport.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transport
        if self.transport:
            _dict['transport'] = self.transport.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DrivingLicenseResponseSchemaDlValidity:
        """Create an instance of DrivingLicenseResponseSchemaDlValidity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DrivingLicenseResponseSchemaDlValidity.parse_obj(obj)

        _obj = DrivingLicenseResponseSchemaDlValidity.parse_obj({
            "non_transport": ValidityDetails.from_dict(obj.get("non_transport")) if obj.get("non_transport") is not None else None,
            "hazardous_valid_till": obj.get("hazardous_valid_till"),
            "transport": ValidityDetails.from_dict(obj.get("transport")) if obj.get("transport") is not None else None,
            "hill_valid_till": obj.get("hill_valid_till")
        })
        return _obj


