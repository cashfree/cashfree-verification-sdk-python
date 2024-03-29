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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from cashfree_verification.models.cin_response_schema_director_details_inner import CinResponseSchemaDirectorDetailsInner

class CinResponseSchema(BaseModel):
    """
    Success response for retrieving CIN information
    """
    verification_id: Optional[StrictStr] = Field(None, description="It displays the unique ID you created to identify the API request.")
    reference_id: Optional[StrictInt] = Field(None, description="It displays the unique ID created by Cashfree Payments for reference purposes.")
    status: Optional[StrictStr] = Field(None, description="It displays the status of the CIN information")
    cin: Optional[StrictStr] = Field(None, description="It displays the entered CIN information.")
    company_name: Optional[StrictStr] = Field(None, description="It displays the name of the company registered under the Ministry of Corporate Affaris.")
    registration_number: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="It displays the registration number of the company.")
    incorporation_date: Optional[StrictStr] = Field(None, description="It displays the date of incorporation of the company.")
    cin_status: Optional[StrictStr] = Field(None, description="It displays the granular level status of the CIN information.")
    email: Optional[StrictStr] = Field(None, description="It displays the email ID of the company registered under the Ministry of Company Affairs.")
    incorporation_country: Optional[StrictStr] = Field(None, description="It displays the name of the country where the company is located.")
    director_details: Optional[conlist(CinResponseSchemaDirectorDetailsInner)] = None
    __properties = ["verification_id", "reference_id", "status", "cin", "company_name", "registration_number", "incorporation_date", "cin_status", "email", "incorporation_country", "director_details"]

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
    def from_json(cls, json_str: str) -> CinResponseSchema:
        """Create an instance of CinResponseSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> CinResponseSchema:
        """Create an instance of CinResponseSchema from a JSON string"""
        temp_dict = json.loads(json_str)
        if "verification_id, reference_id, status, cin, company_name, registration_number, incorporation_date, cin_status, email, incorporation_country, director_details" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in director_details (list)
        _items = []
        if self.director_details:
            for _item in self.director_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['director_details'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CinResponseSchema:
        """Create an instance of CinResponseSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CinResponseSchema.parse_obj(obj)

        _obj = CinResponseSchema.parse_obj({
            "verification_id": obj.get("verification_id"),
            "reference_id": obj.get("reference_id"),
            "status": obj.get("status"),
            "cin": obj.get("cin"),
            "company_name": obj.get("company_name"),
            "registration_number": obj.get("registration_number"),
            "incorporation_date": obj.get("incorporation_date"),
            "cin_status": obj.get("cin_status"),
            "email": obj.get("email"),
            "incorporation_country": obj.get("incorporation_country"),
            "director_details": [CinResponseSchemaDirectorDetailsInner.from_dict(_item) for _item in obj.get("director_details")] if obj.get("director_details") is not None else None
        })
        return _obj


