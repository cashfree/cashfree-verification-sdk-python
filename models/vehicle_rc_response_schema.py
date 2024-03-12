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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from cashfree_verification.models.split_address import SplitAddress

class VehicleRcResponseSchema(BaseModel):
    """
    Verify Vehicle RC success response
    """
    verification_id: Optional[StrictStr] = Field(None, description="It displays the unique ID you created to identify the verification request.")
    reference_id: Optional[StrictInt] = Field(None, description="It displays the unique ID created by Cashfree Payments for reference purposes.")
    status: Optional[StrictStr] = Field(None, description="It displays the status of the vehicle RC information.")
    reg_no: Optional[StrictStr] = Field(None, description="It displays the registration number of the vehicle.")
    var_class: Optional[StrictStr] = Field(None, alias="class", description="It displays the category or type of the vehicle as recognised by the relevant transportation authorities.")
    chassis: Optional[StrictStr] = Field(None, description="It displays the chassis information of the vehicle.")
    engine: Optional[StrictStr] = Field(None, description="It displays the engine number of the vehicle.")
    vehicle_manufacturer_name: Optional[StrictStr] = Field(None, description="It displays the manufacturer of the vehicle.")
    model: Optional[StrictStr] = Field(None, description="It displays the model number of the vehicle.")
    vehicle_color: Optional[StrictStr] = Field(None, description="It displays the colour of the vehicle.")
    type: Optional[StrictStr] = Field(None, description="It displays the type of the vehicle.")
    norms_type: Optional[StrictStr] = Field(None, description="It displays the norms set by the Central Pollution Control Board (CPCB)")
    body_type: Optional[StrictStr] = Field(None, description="It displays the body type of the vehicle.")
    owner_count: Optional[StrictStr] = Field(None, description="It displays the number of owners of the vehicle.")
    owner: Optional[StrictStr] = Field(None, description="It displays the name of the current owner of the vehicle.")
    owner_father_name: Optional[StrictStr] = Field(None, description="It displays the father's name of the current owner of the vehicle.")
    mobile_number: Optional[StrictStr] = Field(None, description="It displays the mobile number of the current owner of the vehicle.")
    rc_status: Optional[StrictStr] = Field(None, description="It displays the status of the RC.")
    status_as_on: Optional[StrictStr] = Field(None, description="It displays the particular date of the status of the RC.")
    reg_authority: Optional[StrictStr] = Field(None, description="It displays the name of the registration authority.")
    reg_date: Optional[StrictStr] = Field(None, description="It displays the date of registration of the vehicle.")
    vehicle_manufacturing_month_year: Optional[StrictStr] = Field(None, description="It displays the month and year of the manufacturing of the vehicle.")
    rc_expiry_date: Optional[StrictStr] = Field(None, description="It displays the date until which the registration of the vehicle is valid.")
    vehicle_tax_upto: Optional[StrictStr] = Field(None, description="It displays the date until which the tax paid by the owner for the vehicle is valid.")
    vehicle_insurance_company_name: Optional[StrictStr] = Field(None, description="It displays the name of the insurance company associated with the vehicle.")
    vehicle_insurance_upto: Optional[StrictStr] = Field(None, description="It displays the date until which the insurance paid by the owner for the vehicle is valid.")
    vehicle_insurance_policy_number: Optional[StrictStr] = Field(None, description="It displays the insurance policy number of the vehicle.")
    rc_financer: Optional[StrictStr] = Field(None, description="It displays the name of the financial institution or lender that provided financing for the purchase of a vehicle.")
    present_address: Optional[StrictStr] = Field(None, description="It displays the current address of the owner of the vehicle.")
    split_present_address: Optional[SplitAddress] = None
    permanent_address: Optional[StrictStr] = Field(None, description="It displays the permanent address of the owner of the vehicle.")
    split_permanent_address: Optional[SplitAddress] = None
    vehicle_cubic_capacity: Optional[StrictStr] = Field(None, description="It displays the cubic capacity of the vehicle's engine.")
    gross_vehicle_weight: Optional[StrictStr] = Field(None, description="It displays the gross weight of the vehicle in kilograms.")
    unladen_weight: Optional[StrictStr] = Field(None, description="It displays the weight of the vehicle without carrying any load in kiolgrams.")
    vehicle_category: Optional[StrictStr] = Field(None, description="It displays the category of the vehicle.")
    rc_standard_cap: Optional[StrictStr] = None
    vehicle_cylinders_no: Optional[StrictStr] = Field(None, description="It displays the number of cylinders present in the vehicle.")
    vehicle_seat_capacity: Optional[StrictStr] = Field(None, description="It displays the number of seats in the vehicle.")
    vehicle_sleeper_capacity: Optional[StrictStr] = Field(None, description="It displays the number of beds available in the vehicle.")
    vehicle_standing_capacity: Optional[StrictStr] = Field(None, description="It displays the number of people that can stand in the vehicle.")
    wheelbase: Optional[StrictStr] = Field(None, description="It displays distance between the front and rear axles of a vehicle in mm.")
    vehicle_number: Optional[StrictStr] = Field(None, description="It displays the registration number of the vehicle.")
    pucc_number: Optional[StrictStr] = Field(None, description="It displays the Pollution Under Control Certificate (PUCC) number associated with vehicle.")
    pucc_upto: Optional[StrictStr] = Field(None, description="It displays till when the PUCC number is valid.")
    blacklist_status: Optional[StrictStr] = Field(None, description="It displays whether the vehicle is blacklisted.")
    blacklist_details: Optional[Dict[str, Any]] = Field(None, description="It displays the reasons for blacklisting the vehicle.")
    challan_details: Optional[Dict[str, Any]] = Field(None, description="It displays traffic tickets or citations issued by traffic police or authorities for various traffic violations.")
    permit_issue_date: Optional[StrictStr] = Field(None, description="It displays when the relevant authorities granted permission or authorisation for a specific type of permit associated with the vehicle.")
    permit_number: Optional[StrictStr] = Field(None, description="It displays the permit number of the vehicle.")
    permit_type: Optional[StrictStr] = Field(None, description="It displays the type of permit issued to the vehicle.")
    permit_valid_from: Optional[StrictStr] = Field(None, description="It displays the beginning date of the issuance of permit.")
    permit_valid_upto: Optional[StrictStr] = Field(None, description="It displays the end date of the permit.")
    non_use_status: Optional[StrictStr] = Field(None, description="It displays whether the vehicle owner or registrant declared that the vehicle is not in use for a certain period.")
    non_use_from: Optional[StrictStr] = Field(None, description="It displays the beginning date of the non use period.")
    non_use_to: Optional[StrictStr] = Field(None, description="It displays the end date of the non use period.")
    national_permit_number: Optional[StrictStr] = Field(None, description="It displays the permit issued to the vehicle to go outside the home state carrying goods.")
    national_permit_upto: Optional[StrictStr] = Field(None, description="It displays the end date of the permit issued to the vechicle to go outside the home state carrying goods.")
    national_permit_issued_by: Optional[StrictStr] = Field(None, description="It displays the national permit issuer's name.")
    is_commercial: Optional[StrictBool] = Field(None, description="It displays whether the vehicle is for commercial purpose.")
    noc_details: Optional[StrictStr] = Field(None, description="It displays the details of the no objection certificate.")
    __properties = ["verification_id", "reference_id", "status", "reg_no", "class", "chassis", "engine", "vehicle_manufacturer_name", "model", "vehicle_color", "type", "norms_type", "body_type", "owner_count", "owner", "owner_father_name", "mobile_number", "rc_status", "status_as_on", "reg_authority", "reg_date", "vehicle_manufacturing_month_year", "rc_expiry_date", "vehicle_tax_upto", "vehicle_insurance_company_name", "vehicle_insurance_upto", "vehicle_insurance_policy_number", "rc_financer", "present_address", "split_present_address", "permanent_address", "split_permanent_address", "vehicle_cubic_capacity", "gross_vehicle_weight", "unladen_weight", "vehicle_category", "rc_standard_cap", "vehicle_cylinders_no", "vehicle_seat_capacity", "vehicle_sleeper_capacity", "vehicle_standing_capacity", "wheelbase", "vehicle_number", "pucc_number", "pucc_upto", "blacklist_status", "blacklist_details", "challan_details", "permit_issue_date", "permit_number", "permit_type", "permit_valid_from", "permit_valid_upto", "non_use_status", "non_use_from", "non_use_to", "national_permit_number", "national_permit_upto", "national_permit_issued_by", "is_commercial", "noc_details"]

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
    def from_json(cls, json_str: str) -> VehicleRcResponseSchema:
        """Create an instance of VehicleRcResponseSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> VehicleRcResponseSchema:
        """Create an instance of VehicleRcResponseSchema from a JSON string"""
        temp_dict = json.loads(json_str)
        if "verification_id, reference_id, status, reg_no, class, chassis, engine, vehicle_manufacturer_name, model, vehicle_color, type, norms_type, body_type, owner_count, owner, owner_father_name, mobile_number, rc_status, status_as_on, reg_authority, reg_date, vehicle_manufacturing_month_year, rc_expiry_date, vehicle_tax_upto, vehicle_insurance_company_name, vehicle_insurance_upto, vehicle_insurance_policy_number, rc_financer, present_address, split_present_address, permanent_address, split_permanent_address, vehicle_cubic_capacity, gross_vehicle_weight, unladen_weight, vehicle_category, rc_standard_cap, vehicle_cylinders_no, vehicle_seat_capacity, vehicle_sleeper_capacity, vehicle_standing_capacity, wheelbase, vehicle_number, pucc_number, pucc_upto, blacklist_status, blacklist_details, challan_details, permit_issue_date, permit_number, permit_type, permit_valid_from, permit_valid_upto, non_use_status, non_use_from, non_use_to, national_permit_number, national_permit_upto, national_permit_issued_by, is_commercial, noc_details" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of split_present_address
        if self.split_present_address:
            _dict['split_present_address'] = self.split_present_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of split_permanent_address
        if self.split_permanent_address:
            _dict['split_permanent_address'] = self.split_permanent_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VehicleRcResponseSchema:
        """Create an instance of VehicleRcResponseSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VehicleRcResponseSchema.parse_obj(obj)

        _obj = VehicleRcResponseSchema.parse_obj({
            "verification_id": obj.get("verification_id"),
            "reference_id": obj.get("reference_id"),
            "status": obj.get("status"),
            "reg_no": obj.get("reg_no"),
            "var_class": obj.get("class"),
            "chassis": obj.get("chassis"),
            "engine": obj.get("engine"),
            "vehicle_manufacturer_name": obj.get("vehicle_manufacturer_name"),
            "model": obj.get("model"),
            "vehicle_color": obj.get("vehicle_color"),
            "type": obj.get("type"),
            "norms_type": obj.get("norms_type"),
            "body_type": obj.get("body_type"),
            "owner_count": obj.get("owner_count"),
            "owner": obj.get("owner"),
            "owner_father_name": obj.get("owner_father_name"),
            "mobile_number": obj.get("mobile_number"),
            "rc_status": obj.get("rc_status"),
            "status_as_on": obj.get("status_as_on"),
            "reg_authority": obj.get("reg_authority"),
            "reg_date": obj.get("reg_date"),
            "vehicle_manufacturing_month_year": obj.get("vehicle_manufacturing_month_year"),
            "rc_expiry_date": obj.get("rc_expiry_date"),
            "vehicle_tax_upto": obj.get("vehicle_tax_upto"),
            "vehicle_insurance_company_name": obj.get("vehicle_insurance_company_name"),
            "vehicle_insurance_upto": obj.get("vehicle_insurance_upto"),
            "vehicle_insurance_policy_number": obj.get("vehicle_insurance_policy_number"),
            "rc_financer": obj.get("rc_financer"),
            "present_address": obj.get("present_address"),
            "split_present_address": SplitAddress.from_dict(obj.get("split_present_address")) if obj.get("split_present_address") is not None else None,
            "permanent_address": obj.get("permanent_address"),
            "split_permanent_address": SplitAddress.from_dict(obj.get("split_permanent_address")) if obj.get("split_permanent_address") is not None else None,
            "vehicle_cubic_capacity": obj.get("vehicle_cubic_capacity"),
            "gross_vehicle_weight": obj.get("gross_vehicle_weight"),
            "unladen_weight": obj.get("unladen_weight"),
            "vehicle_category": obj.get("vehicle_category"),
            "rc_standard_cap": obj.get("rc_standard_cap"),
            "vehicle_cylinders_no": obj.get("vehicle_cylinders_no"),
            "vehicle_seat_capacity": obj.get("vehicle_seat_capacity"),
            "vehicle_sleeper_capacity": obj.get("vehicle_sleeper_capacity"),
            "vehicle_standing_capacity": obj.get("vehicle_standing_capacity"),
            "wheelbase": obj.get("wheelbase"),
            "vehicle_number": obj.get("vehicle_number"),
            "pucc_number": obj.get("pucc_number"),
            "pucc_upto": obj.get("pucc_upto"),
            "blacklist_status": obj.get("blacklist_status"),
            "blacklist_details": obj.get("blacklist_details"),
            "challan_details": obj.get("challan_details"),
            "permit_issue_date": obj.get("permit_issue_date"),
            "permit_number": obj.get("permit_number"),
            "permit_type": obj.get("permit_type"),
            "permit_valid_from": obj.get("permit_valid_from"),
            "permit_valid_upto": obj.get("permit_valid_upto"),
            "non_use_status": obj.get("non_use_status"),
            "non_use_from": obj.get("non_use_from"),
            "non_use_to": obj.get("non_use_to"),
            "national_permit_number": obj.get("national_permit_number"),
            "national_permit_upto": obj.get("national_permit_upto"),
            "national_permit_issued_by": obj.get("national_permit_issued_by"),
            "is_commercial": obj.get("is_commercial"),
            "noc_details": obj.get("noc_details")
        })
        return _obj

