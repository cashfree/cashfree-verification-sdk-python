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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class AadhaarOcrResponseSchema(BaseModel):
    """
    Success response for Aadhaar Verification via OCR
    """
    name: Optional[StrictStr] = Field(None, description="It displays the name of the aadhaar card holder.")
    yob: Optional[StrictStr] = Field(None, description="It displays the year of birth of the aadhaar card holder.")
    father: Optional[StrictStr] = Field(None, description="It displays the father's name of the aadhaar card holder.")
    gender: Optional[StrictStr] = Field(None, description="It displays the gender of the aadhaar card holder.")
    uid: Optional[StrictStr] = Field(None, description="It displays the UID information as present in the aadhaar card.")
    state: Optional[StrictStr] = Field(None, description="It displays the name of the state as present in the aadhaar card.")
    pincode: Optional[StrictStr] = Field(None, description="It displays the PIN code information as present in the aadhaar card.")
    address: Optional[StrictStr] = Field(None, description="It displays the address information of the aadhaar card holder.")
    valid: Optional[StrictBool] = Field(None, description="It displays whether the aadhaar card is valid or not.")
    status: Optional[StrictStr] = Field(None, description="It displays the status of the aadhaar card.")
    reference_id: Optional[StrictStr] = Field(None, description="It displays the unique ID created by Cashfree Payments for reference purposes.")
    verification_id: Optional[StrictStr] = Field(None, description="It displays the unique ID you created to identify this request.")
    confidence_score: Optional[StrictStr] = Field(None, description="It displays the confidence score for this aadhaar card verification request.")
    message: Optional[StrictStr] = Field(None, description="It displays details about the success or failure of the API request.")
    __properties = ["name", "yob", "father", "gender", "uid", "state", "pincode", "address", "valid", "status", "reference_id", "verification_id", "confidence_score", "message"]

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
    def from_json(cls, json_str: str) -> AadhaarOcrResponseSchema:
        """Create an instance of AadhaarOcrResponseSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> AadhaarOcrResponseSchema:
        """Create an instance of AadhaarOcrResponseSchema from a JSON string"""
        temp_dict = json.loads(json_str)
        if "name, yob, father, gender, uid, state, pincode, address, valid, status, reference_id, verification_id, confidence_score, message" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> AadhaarOcrResponseSchema:
        """Create an instance of AadhaarOcrResponseSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AadhaarOcrResponseSchema.parse_obj(obj)

        _obj = AadhaarOcrResponseSchema.parse_obj({
            "name": obj.get("name"),
            "yob": obj.get("yob"),
            "father": obj.get("father"),
            "gender": obj.get("gender"),
            "uid": obj.get("uid"),
            "state": obj.get("state"),
            "pincode": obj.get("pincode"),
            "address": obj.get("address"),
            "valid": obj.get("valid"),
            "status": obj.get("status"),
            "reference_id": obj.get("reference_id"),
            "verification_id": obj.get("verification_id"),
            "confidence_score": obj.get("confidence_score"),
            "message": obj.get("message")
        })
        return _obj

