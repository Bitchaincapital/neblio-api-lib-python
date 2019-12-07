# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class IssueTokenRequestMetadataRules(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'fees': 'IssueTokenRequestMetadataRulesFees',
        'holders': 'list[IssueTokenRequestMetadataRulesHolders]',
        'expiration': 'IssueTokenRequestMetadataRulesExpiration'
    }

    attribute_map = {
        'fees': 'fees',
        'holders': 'holders',
        'expiration': 'expiration'
    }

    def __init__(self, fees=None, holders=None, expiration=None):  # noqa: E501
        """IssueTokenRequestMetadataRules - a model defined in OpenAPI"""  # noqa: E501

        self._fees = None
        self._holders = None
        self._expiration = None
        self.discriminator = None

        if fees is not None:
            self.fees = fees
        if holders is not None:
            self.holders = holders
        if expiration is not None:
            self.expiration = expiration

    @property
    def fees(self):
        """Gets the fees of this IssueTokenRequestMetadataRules.  # noqa: E501


        :return: The fees of this IssueTokenRequestMetadataRules.  # noqa: E501
        :rtype: IssueTokenRequestMetadataRulesFees
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this IssueTokenRequestMetadataRules.


        :param fees: The fees of this IssueTokenRequestMetadataRules.  # noqa: E501
        :type: IssueTokenRequestMetadataRulesFees
        """

        self._fees = fees

    @property
    def holders(self):
        """Gets the holders of this IssueTokenRequestMetadataRules.  # noqa: E501

        Array of objects describing what addresses can hold the token  # noqa: E501

        :return: The holders of this IssueTokenRequestMetadataRules.  # noqa: E501
        :rtype: list[IssueTokenRequestMetadataRulesHolders]
        """
        return self._holders

    @holders.setter
    def holders(self, holders):
        """Sets the holders of this IssueTokenRequestMetadataRules.

        Array of objects describing what addresses can hold the token  # noqa: E501

        :param holders: The holders of this IssueTokenRequestMetadataRules.  # noqa: E501
        :type: list[IssueTokenRequestMetadataRulesHolders]
        """

        self._holders = holders

    @property
    def expiration(self):
        """Gets the expiration of this IssueTokenRequestMetadataRules.  # noqa: E501


        :return: The expiration of this IssueTokenRequestMetadataRules.  # noqa: E501
        :rtype: IssueTokenRequestMetadataRulesExpiration
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this IssueTokenRequestMetadataRules.


        :param expiration: The expiration of this IssueTokenRequestMetadataRules.  # noqa: E501
        :type: IssueTokenRequestMetadataRulesExpiration
        """

        self._expiration = expiration

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IssueTokenRequestMetadataRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
