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
from pydantic import BaseModel, Field, StrictStr, conlist
from cashfree_verification.models.bulk_pan_request_schema_entries_inner import BulkPanRequestSchemaEntriesInner

class BulkPanRequestSchema(BaseModel):
    """
    Find the request parameters to verify a large number of PAN information
    """
    bulk_verification_id: Optional[StrictStr] = Field('ABCPV1234D', description="It is the unique ID you create to identify the API request. Only alphanumeric and underscore ( _ ) are allowed.")
    entries: Optional[conlist(BulkPanRequestSchemaEntriesInner, min_items=2)] = Field(None, description="It is the array of PAN details for verification. PAN and name should be included. The name parameter is optional.")
    __properties = ["bulk_verification_id", "entries"]

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
    def from_json(cls, json_str: str) -> BulkPanRequestSchema:
        """Create an instance of BulkPanRequestSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> BulkPanRequestSchema:
        """Create an instance of BulkPanRequestSchema from a JSON string"""
        temp_dict = json.loads(json_str)
        if "bulk_verification_id, entries" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in entries (list)
        _items = []
        if self.entries:
            for _item in self.entries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entries'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BulkPanRequestSchema:
        """Create an instance of BulkPanRequestSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BulkPanRequestSchema.parse_obj(obj)

        _obj = BulkPanRequestSchema.parse_obj({
            "bulk_verification_id": obj.get("bulk_verification_id") if obj.get("bulk_verification_id") is not None else 'ABCPV1234D',
            "entries": [BulkPanRequestSchemaEntriesInner.from_dict(_item) for _item in obj.get("entries")] if obj.get("entries") is not None else None
        })
        return _obj

