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


from typing import Union
from pydantic import BaseModel, Field, StrictBytes, StrictStr

class ESignVerificationUploadDocumentRequestSchema(BaseModel):
    """
    Find the request parameters to upload the document that requires an e-signature.
    """
    document: Union[StrictBytes, StrictStr] = Field(..., description="Upload the document that requires an e-sign. Allowed file type - PDF. Max file size allowed - 10MB.")
    __properties = ["document"]

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
    def from_json(cls, json_str: str) -> ESignVerificationUploadDocumentRequestSchema:
        """Create an instance of ESignVerificationUploadDocumentRequestSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> ESignVerificationUploadDocumentRequestSchema:
        """Create an instance of ESignVerificationUploadDocumentRequestSchema from a JSON string"""
        temp_dict = json.loads(json_str)
        if "document" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> ESignVerificationUploadDocumentRequestSchema:
        """Create an instance of ESignVerificationUploadDocumentRequestSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ESignVerificationUploadDocumentRequestSchema.parse_obj(obj)

        _obj = ESignVerificationUploadDocumentRequestSchema.parse_obj({
            "document": obj.get("document")
        })
        return _obj


