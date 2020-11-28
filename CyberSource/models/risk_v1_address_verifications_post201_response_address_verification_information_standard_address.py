# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address1': 'RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddressAddress1',
        'address2': 'str',
        'address3': 'str',
        'address4': 'str',
        'locality': 'str',
        'county': 'str',
        'country': 'str',
        'csz': 'str',
        'iso_country': 'str',
        'administrative_area': 'str',
        'postal_code': 'str'
    }

    attribute_map = {
        'address1': 'address1',
        'address2': 'address2',
        'address3': 'address3',
        'address4': 'address4',
        'locality': 'locality',
        'county': 'county',
        'country': 'country',
        'csz': 'csz',
        'iso_country': 'isoCountry',
        'administrative_area': 'administrativeArea',
        'postal_code': 'postalCode'
    }

    def __init__(self, address1=None, address2=None, address3=None, address4=None, locality=None, county=None, country=None, csz=None, iso_country=None, administrative_area=None, postal_code=None):
        """
        RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress - a model defined in Swagger
        """

        self._address1 = None
        self._address2 = None
        self._address3 = None
        self._address4 = None
        self._locality = None
        self._county = None
        self._country = None
        self._csz = None
        self._iso_country = None
        self._administrative_area = None
        self._postal_code = None

        if address1 is not None:
          self.address1 = address1
        if address2 is not None:
          self.address2 = address2
        if address3 is not None:
          self.address3 = address3
        if address4 is not None:
          self.address4 = address4
        if locality is not None:
          self.locality = locality
        if county is not None:
          self.county = county
        if country is not None:
          self.country = country
        if csz is not None:
          self.csz = csz
        if iso_country is not None:
          self.iso_country = iso_country
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if postal_code is not None:
          self.postal_code = postal_code

    @property
    def address1(self):
        """
        Gets the address1 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.

        :return: The address1 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :rtype: RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddressAddress1
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.

        :param address1: The address1 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :type: RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddressAddress1
        """

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Second line of the standardized address.

        :return: The address2 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Second line of the standardized address.

        :param address2: The address2 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :type: str
        """

        self._address2 = address2

    @property
    def address3(self):
        """
        Gets the address3 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Third line of the standardized address.

        :return: The address3 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :rtype: str
        """
        return self._address3

    @address3.setter
    def address3(self, address3):
        """
        Sets the address3 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Third line of the standardized address.

        :param address3: The address3 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :type: str
        """

        self._address3 = address3

    @property
    def address4(self):
        """
        Gets the address4 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Fourth line of the standardized address.

        :return: The address4 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :rtype: str
        """
        return self._address4

    @address4.setter
    def address4(self, address4):
        """
        Sets the address4 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Fourth line of the standardized address.

        :param address4: The address4 of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :type: str
        """

        self._address4 = address4

    @property
    def locality(self):
        """
        Gets the locality of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Standardized city name.

        :return: The locality of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Standardized city name.

        :param locality: The locality of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :type: str
        """

        self._locality = locality

    @property
    def county(self):
        """
        Gets the county of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        U.S. county if available.

        :return: The county of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """
        Sets the county of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        U.S. county if available.

        :param county: The county of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :type: str
        """

        self._county = county

    @property
    def country(self):
        """
        Gets the country of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Standardized country name.

        :return: The country of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Standardized country name.

        :param country: The country of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :type: str
        """

        self._country = country

    @property
    def csz(self):
        """
        Gets the csz of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Standardized city, state or province, and ZIP +4 code or postal code line.

        :return: The csz of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :rtype: str
        """
        return self._csz

    @csz.setter
    def csz(self, csz):
        """
        Sets the csz of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Standardized city, state or province, and ZIP +4 code or postal code line.

        :param csz: The csz of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :type: str
        """

        self._csz = csz

    @property
    def iso_country(self):
        """
        Gets the iso_country of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Standardized two-character ISO country code.

        :return: The iso_country of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :rtype: str
        """
        return self._iso_country

    @iso_country.setter
    def iso_country(self, iso_country):
        """
        Sets the iso_country of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Standardized two-character ISO country code.

        :param iso_country: The iso_country of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :type: str
        """

        self._iso_country = iso_country

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        U.S.P.S. standardized state or province abbreviation.

        :return: The administrative_area of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        U.S.P.S. standardized state or province abbreviation.

        :param administrative_area: The administrative_area of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :type: str
        """

        self._administrative_area = administrative_area

    @property
    def postal_code(self):
        """
        Gets the postal_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Standardized U.S. ZIP + 4 postal code.

        :return: The postal_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        Standardized U.S. ZIP + 4 postal code.

        :param postal_code: The postal_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress.
        :type: str
        """

        self._postal_code = postal_code

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
