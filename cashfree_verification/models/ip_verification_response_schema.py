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

class IpVerificationResponseSchema(BaseModel):
    """
    Verify IP success response
    """
    reference_id: Optional[StrictInt] = Field(None, description="It displays the unique ID created by Cashfree Payments for reference purposes.")
    verification_id: Optional[StrictStr] = Field(None, description="It displays the unique ID you created to identify the verification request.")
    status: Optional[StrictStr] = Field(None, description="It displays the status of the IP address.")
    ip_address: Optional[StrictStr] = Field(None, description="It displays the entered IP address.")
    proxy_type: Optional[StrictStr] = Field(None, description="It displays the category or classification of a proxy server based on its functionality and how it handles network requests.")
    country_code: Optional[StrictStr] = Field(None, description="It displays the country code associated with the geographical location of the device or network to which the IP address is assigned.")
    country_name: Optional[StrictStr] = Field(None, description="It displays the name of the country associated with the geographical location of the device or network to which the IP address is assigned.")
    region_name: Optional[StrictStr] = Field(None, description="It displays the name of the region associated with the geographical location of the device or network to which the IP address is assigned.")
    city_name: Optional[StrictStr] = Field(None, description="It displays the name of the city associated with the geographical location of the device or network to which the IP address is assigned.")
    city_risk_score: Optional[StrictStr] = Field(None, description="It displays the risk score associated with a particular city based on factors such as cybersecurity threats, crime rates, or other relevant data.")
    proxy_type_risk_score: Optional[StrictStr] = Field(None, description="It displays the risk score associated with a particular city based on factors such as cybersecurity threats, crime rates, or other relevant data.")
    __properties = ["reference_id", "verification_id", "status", "ip_address", "proxy_type", "country_code", "country_name", "region_name", "city_name", "city_risk_score", "proxy_type_risk_score"]

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
    def from_json(cls, json_str: str) -> IpVerificationResponseSchema:
        """Create an instance of IpVerificationResponseSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> IpVerificationResponseSchema:
        """Create an instance of IpVerificationResponseSchema from a JSON string"""
        temp_dict = json.loads(json_str)
        if "reference_id, verification_id, status, ip_address, proxy_type, country_code, country_name, region_name, city_name, city_risk_score, proxy_type_risk_score" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> IpVerificationResponseSchema:
        """Create an instance of IpVerificationResponseSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IpVerificationResponseSchema.parse_obj(obj)

        _obj = IpVerificationResponseSchema.parse_obj({
            "reference_id": obj.get("reference_id"),
            "verification_id": obj.get("verification_id"),
            "status": obj.get("status"),
            "ip_address": obj.get("ip_address"),
            "proxy_type": obj.get("proxy_type"),
            "country_code": obj.get("country_code"),
            "country_name": obj.get("country_name"),
            "region_name": obj.get("region_name"),
            "city_name": obj.get("city_name"),
            "city_risk_score": obj.get("city_risk_score"),
            "proxy_type_risk_score": obj.get("proxy_type_risk_score")
        })
        return _obj


