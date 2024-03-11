# coding: utf-8

"""
    Cashfree Verification API's.

    Cashfree's Verification APIs provide different types of verification to our merchants.

    The version of the OpenAPI document: 2023-12-18
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import cashfree_verification
from cashfree_verification.models.vehicle_rc_response_schema import VehicleRcResponseSchema  # noqa: E501
from cashfree_verification.rest import ApiException

class TestVehicleRcResponseSchema(unittest.TestCase):
    """VehicleRcResponseSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VehicleRcResponseSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VehicleRcResponseSchema`
        """
        model = cashfree_verification.models.vehicle_rc_response_schema.VehicleRcResponseSchema()  # noqa: E501
        if include_optional :
            return VehicleRcResponseSchema(
                verification_id = '6c617137-6d50-4c59-9302-c453ca42aa8589', 
                reference_id = 88, 
                status = 'VALID', 
                reg_no = 'KA01MW6127', 
                var_class = 'Motor Car', 
                chassis = 'MALBK511VMM110528', 
                engine = 'G3LCMM440323', 
                vehicle_manufacturer_name = 'HYUNDAI MOTOR INDIA LTD', 
                model = 'I20 N LINE N8 1.0TURBO GDI DCT', 
                vehicle_color = 'TITAN GREY', 
                type = 'PETROL', 
                norms_type = 'BHARAT STAGE VI', 
                body_type = 'HATCHBACK', 
                owner_count = '1', 
                owner = 'RAGHAV RASTOGI', 
                owner_father_name = 'ROHIT RASTOGI', 
                mobile_number = '', 
                rc_status = 'ACTIVE', 
                status_as_on = '19/01/2024', 
                reg_authority = 'BENGALURU CENTRAL RTO, Karnataka', 
                reg_date = '24/12/2021', 
                vehicle_manufacturing_month_year = '12/2021', 
                rc_expiry_date = '23/12/2036', 
                vehicle_tax_upto = '', 
                vehicle_insurance_company_name = 'TATA AIG GENERAL INSURANCE CO. LTD.', 
                vehicle_insurance_upto = '14/12/2024', 
                vehicle_insurance_policy_number = '62000344820000', 
                rc_financer = 'BANDHAN BANK', 
                present_address = 'FLAT # 901 A BLOCK GOYAL ORCHID, LAKE VIEW APTS KARIAGRAHARA, BELLANDUR, Bangalore, Karnataka, 560103', 
                split_present_address = {"value":{"district":["BANGALORE"],"state":["KARNATAKA","KA"],"city":["BELLANDUR"],"pincode":"560103","country":["IN","IND","INDIA"],"address_line":"FLAT 901 A BLOCK GOYAL ORCHID,LAKE VIEW APTS KARIAGRAHARA"}}, 
                permanent_address = 'FLAT # 901 A BLOCK GOYAL ORCHID, LAKE VIEW APTS KARIAGRAHARA, BELLANDUR, Bangalore, Karnataka, 560103', 
                split_permanent_address = {"value":{"district":["BANGALORE"],"state":["KARNATAKA","KA"],"city":["BELLANDUR"],"pincode":"560103","country":["IN","IND","INDIA"],"address_line":"FLAT 901 A BLOCK GOYAL ORCHID,LAKE VIEW APTS KARIAGRAHARA"}}, 
                vehicle_cubic_capacity = '998', 
                gross_vehicle_weight = '1490', 
                unladen_weight = '1086', 
                vehicle_category = 'LMV', 
                rc_standard_cap = '0', 
                vehicle_cylinders_no = '3', 
                vehicle_seat_capacity = '5', 
                vehicle_sleeper_capacity = '0', 
                vehicle_standing_capacity = '0', 
                wheelbase = '2580', 
                vehicle_number = 'KA01MW6127', 
                pucc_number = 'Newv4', 
                pucc_upto = '23/12/2022', 
                blacklist_status = 'NA', 
                blacklist_details = None, 
                challan_details = None, 
                permit_issue_date = '', 
                permit_number = '', 
                permit_type = '', 
                permit_valid_from = '', 
                permit_valid_upto = '', 
                non_use_status = '', 
                non_use_from = '', 
                non_use_to = '', 
                national_permit_number = '', 
                national_permit_upto = '', 
                national_permit_issued_by = '', 
                is_commercial = False, 
                noc_details = ''
            )
        else :
            return VehicleRcResponseSchema(
        )
        """

    def testVehicleRcResponseSchema(self):
        """Test VehicleRcResponseSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()