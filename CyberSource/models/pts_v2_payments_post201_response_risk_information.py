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


class PtsV2PaymentsPost201ResponseRiskInformation(object):
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
        'profile': 'PtsV2PaymentsPost201ResponseRiskInformationProfile',
        'rules': 'list[PtsV2PaymentsPost201ResponseRiskInformationRules]',
        'info_codes': 'PtsV2PaymentsPost201ResponseRiskInformationInfoCodes',
        'velocity': 'PtsV2PaymentsPost201ResponseRiskInformationVelocity',
        'case_priority': 'int',
        'local_time': 'str',
        'score': 'PtsV2PaymentsPost201ResponseRiskInformationScore',
        'ip_address': 'PtsV2PaymentsPost201ResponseRiskInformationIpAddress',
        'providers': 'PtsV2PaymentsPost201ResponseRiskInformationProviders',
        'travel': 'PtsV2PaymentsPost201ResponseRiskInformationTravel'
    }

    attribute_map = {
        'profile': 'profile',
        'rules': 'rules',
        'info_codes': 'infoCodes',
        'velocity': 'velocity',
        'case_priority': 'casePriority',
        'local_time': 'localTime',
        'score': 'score',
        'ip_address': 'ipAddress',
        'providers': 'providers',
        'travel': 'travel'
    }

    def __init__(self, profile=None, rules=None, info_codes=None, velocity=None, case_priority=None, local_time=None, score=None, ip_address=None, providers=None, travel=None):
        """
        PtsV2PaymentsPost201ResponseRiskInformation - a model defined in Swagger
        """

        self._profile = None
        self._rules = None
        self._info_codes = None
        self._velocity = None
        self._case_priority = None
        self._local_time = None
        self._score = None
        self._ip_address = None
        self._providers = None
        self._travel = None

        if profile is not None:
          self.profile = profile
        if rules is not None:
          self.rules = rules
        if info_codes is not None:
          self.info_codes = info_codes
        if velocity is not None:
          self.velocity = velocity
        if case_priority is not None:
          self.case_priority = case_priority
        if local_time is not None:
          self.local_time = local_time
        if score is not None:
          self.score = score
        if ip_address is not None:
          self.ip_address = ip_address
        if providers is not None:
          self.providers = providers
        if travel is not None:
          self.travel = travel

    @property
    def profile(self):
        """
        Gets the profile of this PtsV2PaymentsPost201ResponseRiskInformation.

        :return: The profile of this PtsV2PaymentsPost201ResponseRiskInformation.
        :rtype: PtsV2PaymentsPost201ResponseRiskInformationProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """
        Sets the profile of this PtsV2PaymentsPost201ResponseRiskInformation.

        :param profile: The profile of this PtsV2PaymentsPost201ResponseRiskInformation.
        :type: PtsV2PaymentsPost201ResponseRiskInformationProfile
        """

        self._profile = profile

    @property
    def rules(self):
        """
        Gets the rules of this PtsV2PaymentsPost201ResponseRiskInformation.

        :return: The rules of this PtsV2PaymentsPost201ResponseRiskInformation.
        :rtype: list[PtsV2PaymentsPost201ResponseRiskInformationRules]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this PtsV2PaymentsPost201ResponseRiskInformation.

        :param rules: The rules of this PtsV2PaymentsPost201ResponseRiskInformation.
        :type: list[PtsV2PaymentsPost201ResponseRiskInformationRules]
        """

        self._rules = rules

    @property
    def info_codes(self):
        """
        Gets the info_codes of this PtsV2PaymentsPost201ResponseRiskInformation.

        :return: The info_codes of this PtsV2PaymentsPost201ResponseRiskInformation.
        :rtype: PtsV2PaymentsPost201ResponseRiskInformationInfoCodes
        """
        return self._info_codes

    @info_codes.setter
    def info_codes(self, info_codes):
        """
        Sets the info_codes of this PtsV2PaymentsPost201ResponseRiskInformation.

        :param info_codes: The info_codes of this PtsV2PaymentsPost201ResponseRiskInformation.
        :type: PtsV2PaymentsPost201ResponseRiskInformationInfoCodes
        """

        self._info_codes = info_codes

    @property
    def velocity(self):
        """
        Gets the velocity of this PtsV2PaymentsPost201ResponseRiskInformation.

        :return: The velocity of this PtsV2PaymentsPost201ResponseRiskInformation.
        :rtype: PtsV2PaymentsPost201ResponseRiskInformationVelocity
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """
        Sets the velocity of this PtsV2PaymentsPost201ResponseRiskInformation.

        :param velocity: The velocity of this PtsV2PaymentsPost201ResponseRiskInformation.
        :type: PtsV2PaymentsPost201ResponseRiskInformationVelocity
        """

        self._velocity = velocity

    @property
    def case_priority(self):
        """
        Gets the case_priority of this PtsV2PaymentsPost201ResponseRiskInformation.
        You receive this field only if you subscribe to the Enhanced Case Management service. The priority level ranges from 1 (highest) to 5 (lowest); the default value is 3. If you do not assign a priority to your rules or to your profiles, the default value is given to the order.  For all possible values, see the `decision_case_priority` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The case_priority of this PtsV2PaymentsPost201ResponseRiskInformation.
        :rtype: int
        """
        return self._case_priority

    @case_priority.setter
    def case_priority(self, case_priority):
        """
        Sets the case_priority of this PtsV2PaymentsPost201ResponseRiskInformation.
        You receive this field only if you subscribe to the Enhanced Case Management service. The priority level ranges from 1 (highest) to 5 (lowest); the default value is 3. If you do not assign a priority to your rules or to your profiles, the default value is given to the order.  For all possible values, see the `decision_case_priority` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param case_priority: The case_priority of this PtsV2PaymentsPost201ResponseRiskInformation.
        :type: int
        """

        self._case_priority = case_priority

    @property
    def local_time(self):
        """
        Gets the local_time of this PtsV2PaymentsPost201ResponseRiskInformation.
        The customer's local time (`hh:mm:ss`), which is calculated from the transaction request time and the customer's billing address.  For details, see the `score_time_local` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) 

        :return: The local_time of this PtsV2PaymentsPost201ResponseRiskInformation.
        :rtype: str
        """
        return self._local_time

    @local_time.setter
    def local_time(self, local_time):
        """
        Sets the local_time of this PtsV2PaymentsPost201ResponseRiskInformation.
        The customer's local time (`hh:mm:ss`), which is calculated from the transaction request time and the customer's billing address.  For details, see the `score_time_local` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) 

        :param local_time: The local_time of this PtsV2PaymentsPost201ResponseRiskInformation.
        :type: str
        """

        self._local_time = local_time

    @property
    def score(self):
        """
        Gets the score of this PtsV2PaymentsPost201ResponseRiskInformation.

        :return: The score of this PtsV2PaymentsPost201ResponseRiskInformation.
        :rtype: PtsV2PaymentsPost201ResponseRiskInformationScore
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this PtsV2PaymentsPost201ResponseRiskInformation.

        :param score: The score of this PtsV2PaymentsPost201ResponseRiskInformation.
        :type: PtsV2PaymentsPost201ResponseRiskInformationScore
        """

        self._score = score

    @property
    def ip_address(self):
        """
        Gets the ip_address of this PtsV2PaymentsPost201ResponseRiskInformation.

        :return: The ip_address of this PtsV2PaymentsPost201ResponseRiskInformation.
        :rtype: PtsV2PaymentsPost201ResponseRiskInformationIpAddress
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this PtsV2PaymentsPost201ResponseRiskInformation.

        :param ip_address: The ip_address of this PtsV2PaymentsPost201ResponseRiskInformation.
        :type: PtsV2PaymentsPost201ResponseRiskInformationIpAddress
        """

        self._ip_address = ip_address

    @property
    def providers(self):
        """
        Gets the providers of this PtsV2PaymentsPost201ResponseRiskInformation.

        :return: The providers of this PtsV2PaymentsPost201ResponseRiskInformation.
        :rtype: PtsV2PaymentsPost201ResponseRiskInformationProviders
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        """
        Sets the providers of this PtsV2PaymentsPost201ResponseRiskInformation.

        :param providers: The providers of this PtsV2PaymentsPost201ResponseRiskInformation.
        :type: PtsV2PaymentsPost201ResponseRiskInformationProviders
        """

        self._providers = providers

    @property
    def travel(self):
        """
        Gets the travel of this PtsV2PaymentsPost201ResponseRiskInformation.

        :return: The travel of this PtsV2PaymentsPost201ResponseRiskInformation.
        :rtype: PtsV2PaymentsPost201ResponseRiskInformationTravel
        """
        return self._travel

    @travel.setter
    def travel(self, travel):
        """
        Sets the travel of this PtsV2PaymentsPost201ResponseRiskInformation.

        :param travel: The travel of this PtsV2PaymentsPost201ResponseRiskInformation.
        :type: PtsV2PaymentsPost201ResponseRiskInformationTravel
        """

        self._travel = travel

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseRiskInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
