# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IssueTokenRequestMetadataRulesHolders(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'address': 'str',
        'locked': 'bool'
    }

    attribute_map = {
        'address': 'address',
        'locked': 'locked'
    }

    def __init__(self, address=None, locked=None):  # noqa: E501
        """IssueTokenRequestMetadataRulesHolders - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._locked = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if locked is not None:
            self.locked = locked

    @property
    def address(self):
        """Gets the address of this IssueTokenRequestMetadataRulesHolders.  # noqa: E501

        Address that can hold the token  # noqa: E501

        :return: The address of this IssueTokenRequestMetadataRulesHolders.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IssueTokenRequestMetadataRulesHolders.

        Address that can hold the token  # noqa: E501

        :param address: The address of this IssueTokenRequestMetadataRulesHolders.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def locked(self):
        """Gets the locked of this IssueTokenRequestMetadataRulesHolders.  # noqa: E501

        Whether this rule can be modified in future transactions  # noqa: E501

        :return: The locked of this IssueTokenRequestMetadataRulesHolders.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this IssueTokenRequestMetadataRulesHolders.

        Whether this rule can be modified in future transactions  # noqa: E501

        :param locked: The locked of this IssueTokenRequestMetadataRulesHolders.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, IssueTokenRequestMetadataRulesHolders):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
