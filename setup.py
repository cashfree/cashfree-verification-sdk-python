# coding: utf-8

"""
    Cashfree Verification API's.

    Cashfree's Verification APIs provide different types of verification to our merchants.

    The version of the OpenAPI document: 2023-12-18
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "cashfree_verification"
VERSION = "2.0.0"
with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "sentry-sdk >= 1.32.0, < 1.33.0",
    "pydantic >= 1.10.5, < 2",
    "aenum"
]

setup(
    name=NAME,
    version=VERSION,
    description="Cashfree Verification API&#39;s.",
    author="Cashfree Payments",
    author_email="developers@cashfree.com",
    url="https://cashfree.com",
    keywords=["Payment Gateway", "Cashfree", "SDK", "Payments", "Cashfree Verification API's."],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description_content_type='text/markdown',
    long_description=readme,
    package_data={"cashfree_verification": ["py.typed"]},
)
