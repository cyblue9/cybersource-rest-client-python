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


class Vasv2taxOrderInformationBillTo(object):
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
        'address1': 'str',
        'address2': 'str',
        'locality': 'str',
        'administrative_area': 'str',
        'postal_code': 'str',
        'country': 'str'
    }

    attribute_map = {
        'address1': 'address1',
        'address2': 'address2',
        'locality': 'locality',
        'administrative_area': 'administrativeArea',
        'postal_code': 'postalCode',
        'country': 'country'
    }

    def __init__(self, address1=None, address2=None, locality=None, administrative_area=None, postal_code=None, country=None):
        """
        Vasv2taxOrderInformationBillTo - a model defined in Swagger
        """

        self._address1 = None
        self._address2 = None
        self._locality = None
        self._administrative_area = None
        self._postal_code = None
        self._country = None

        if address1 is not None:
          self.address1 = address1
        if address2 is not None:
          self.address2 = address2
        if locality is not None:
          self.locality = locality
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if postal_code is not None:
          self.postal_code = postal_code
        if country is not None:
          self.country = country

    @property
    def address1(self):
        """
        Gets the address1 of this Vasv2taxOrderInformationBillTo.
        First line of the billing street address.  #### Tax Calculation Required for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :return: The address1 of this Vasv2taxOrderInformationBillTo.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Vasv2taxOrderInformationBillTo.
        First line of the billing street address.  #### Tax Calculation Required for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :param address1: The address1 of this Vasv2taxOrderInformationBillTo.
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this Vasv2taxOrderInformationBillTo.
        Second line of the billing street address.  #### Tax Calculation Optional for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :return: The address2 of this Vasv2taxOrderInformationBillTo.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this Vasv2taxOrderInformationBillTo.
        Second line of the billing street address.  #### Tax Calculation Optional for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :param address2: The address2 of this Vasv2taxOrderInformationBillTo.
        :type: str
        """

        self._address2 = address2

    @property
    def locality(self):
        """
        Gets the locality of this Vasv2taxOrderInformationBillTo.
        Credit card billing city.  #### Tax Calculation Required for U.S. and Canadian taxes only. Not applicable to international and value added taxes. 

        :return: The locality of this Vasv2taxOrderInformationBillTo.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Vasv2taxOrderInformationBillTo.
        Credit card billing city.  #### Tax Calculation Required for U.S. and Canadian taxes only. Not applicable to international and value added taxes. 

        :param locality: The locality of this Vasv2taxOrderInformationBillTo.
        :type: str
        """

        self._locality = locality

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Vasv2taxOrderInformationBillTo.
        Credit card billing state or province.  #### Tax Calculation Required for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :return: The administrative_area of this Vasv2taxOrderInformationBillTo.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Vasv2taxOrderInformationBillTo.
        Credit card billing state or province.  #### Tax Calculation Required for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :param administrative_area: The administrative_area of this Vasv2taxOrderInformationBillTo.
        :type: str
        """

        self._administrative_area = administrative_area

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Vasv2taxOrderInformationBillTo.
        Postal code for the billing address. The postal code must consist of 5 to 9 digits. If the billing country is the U.S., the 9-digit postal code must follow this format:  [5 digits][dash][4 digits]  **Example**: 12345-6789  If the billing country is Canada, the 6-digit postal code must follow this format:  [alpha][numeric][alpha] [numeric][alpha][numeric]  **Example**: A1B 2C3  #### Tax Calculation Required for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :return: The postal_code of this Vasv2taxOrderInformationBillTo.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Vasv2taxOrderInformationBillTo.
        Postal code for the billing address. The postal code must consist of 5 to 9 digits. If the billing country is the U.S., the 9-digit postal code must follow this format:  [5 digits][dash][4 digits]  **Example**: 12345-6789  If the billing country is Canada, the 6-digit postal code must follow this format:  [alpha][numeric][alpha] [numeric][alpha][numeric]  **Example**: A1B 2C3  #### Tax Calculation Required for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :param postal_code: The postal_code of this Vasv2taxOrderInformationBillTo.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """
        Gets the country of this Vasv2taxOrderInformationBillTo.
        Credit card billing country. Use the [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf).  If `orderInformation.shipTo.country` is not provided, `orderInformation.billTo.country` is used in its place. If  `orderInformation.billTo.country` is set to `US` or `CA`, then `orderInformation.billTo.postalCode` and `orderInformation.billTo.administrativeArea` are also required.  #### Tax Calculation Required for U.S., Canadian, international and value added taxes. 

        :return: The country of this Vasv2taxOrderInformationBillTo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Vasv2taxOrderInformationBillTo.
        Credit card billing country. Use the [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf).  If `orderInformation.shipTo.country` is not provided, `orderInformation.billTo.country` is used in its place. If  `orderInformation.billTo.country` is set to `US` or `CA`, then `orderInformation.billTo.postalCode` and `orderInformation.billTo.administrativeArea` are also required.  #### Tax Calculation Required for U.S., Canadian, international and value added taxes. 

        :param country: The country of this Vasv2taxOrderInformationBillTo.
        :type: str
        """

        self._country = country

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
        if not isinstance(other, Vasv2taxOrderInformationBillTo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
