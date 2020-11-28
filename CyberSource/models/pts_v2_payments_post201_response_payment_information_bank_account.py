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


class PtsV2PaymentsPost201ResponsePaymentInformationBankAccount(object):
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
        'corrected_account_number': 'str'
    }

    attribute_map = {
        'corrected_account_number': 'correctedAccountNumber'
    }

    def __init__(self, corrected_account_number=None):
        """
        PtsV2PaymentsPost201ResponsePaymentInformationBankAccount - a model defined in Swagger
        """

        self._corrected_account_number = None

        if corrected_account_number is not None:
          self.corrected_account_number = corrected_account_number

    @property
    def corrected_account_number(self):
        """
        Gets the corrected_account_number of this PtsV2PaymentsPost201ResponsePaymentInformationBankAccount.
        Corrected account number from the ACH verification service.  For details, see `ecp_debit_corrected_account_number` or `ecp_credit_corrected_account_number` field descriptions in [Electronic Check Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/) 

        :return: The corrected_account_number of this PtsV2PaymentsPost201ResponsePaymentInformationBankAccount.
        :rtype: str
        """
        return self._corrected_account_number

    @corrected_account_number.setter
    def corrected_account_number(self, corrected_account_number):
        """
        Sets the corrected_account_number of this PtsV2PaymentsPost201ResponsePaymentInformationBankAccount.
        Corrected account number from the ACH verification service.  For details, see `ecp_debit_corrected_account_number` or `ecp_credit_corrected_account_number` field descriptions in [Electronic Check Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/) 

        :param corrected_account_number: The corrected_account_number of this PtsV2PaymentsPost201ResponsePaymentInformationBankAccount.
        :type: str
        """

        self._corrected_account_number = corrected_account_number

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
        if not isinstance(other, PtsV2PaymentsPost201ResponsePaymentInformationBankAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
