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
from cashfree_verification.models.advance_employment_response_recent_employment_details_employee_details_epfo import AdvanceEmploymentResponseRecentEmploymentDetailsEmployeeDetailsEpfo

class AdvanceEmploymentResponseRecentEmploymentDetailsEmployeeDetails(BaseModel):
    """
    It contains the details of the individual as an employee.
    """
    member_id: Optional[StrictStr] = Field(None, description="It displays the unique ID assigned to an individual.")
    exit_date: Optional[StrictStr] = Field(None, description="It displays the last working day of the employee in the organisation.")
    joining_date: Optional[StrictStr] = Field(None, description="It displays the first working day of the employee in the organisation.")
    uan: Optional[StrictStr] = Field(None, description="It displays the Universal Account Number (UAN) information of the employee.")
    epfo: Optional[AdvanceEmploymentResponseRecentEmploymentDetailsEmployeeDetailsEpfo] = None
    employed: Optional[StrictBool] = Field(None, description="It displays whether the individual is employed.")
    employee_name_match: Optional[StrictBool] = Field(None, description="It displays whether the individual's name matches with the name found in EPFO.")
    exit_date_marked: Optional[StrictBool] = Field(None, description="It displays whether the last working  ")
    __properties = ["member_id", "exit_date", "joining_date", "uan", "epfo", "employed", "employee_name_match", "exit_date_marked"]

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
    def from_json(cls, json_str: str) -> AdvanceEmploymentResponseRecentEmploymentDetailsEmployeeDetails:
        """Create an instance of AdvanceEmploymentResponseRecentEmploymentDetailsEmployeeDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> AdvanceEmploymentResponseRecentEmploymentDetailsEmployeeDetails:
        """Create an instance of AdvanceEmploymentResponseRecentEmploymentDetailsEmployeeDetails from a JSON string"""
        temp_dict = json.loads(json_str)
        if "member_id, exit_date, joining_date, uan, epfo, employed, employee_name_match, exit_date_marked" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of epfo
        if self.epfo:
            _dict['epfo'] = self.epfo.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdvanceEmploymentResponseRecentEmploymentDetailsEmployeeDetails:
        """Create an instance of AdvanceEmploymentResponseRecentEmploymentDetailsEmployeeDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdvanceEmploymentResponseRecentEmploymentDetailsEmployeeDetails.parse_obj(obj)

        _obj = AdvanceEmploymentResponseRecentEmploymentDetailsEmployeeDetails.parse_obj({
            "member_id": obj.get("member_id"),
            "exit_date": obj.get("exit_date"),
            "joining_date": obj.get("joining_date"),
            "uan": obj.get("uan"),
            "epfo": AdvanceEmploymentResponseRecentEmploymentDetailsEmployeeDetailsEpfo.from_dict(obj.get("epfo")) if obj.get("epfo") is not None else None,
            "employed": obj.get("employed"),
            "employee_name_match": obj.get("employee_name_match"),
            "exit_date_marked": obj.get("exit_date_marked")
        })
        return _obj


