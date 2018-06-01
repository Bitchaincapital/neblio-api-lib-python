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

from swagger_client.models.issue_token_request_flags import IssueTokenRequestFlags  # noqa: F401,E501
from swagger_client.models.issue_token_request_metadata import IssueTokenRequestMetadata  # noqa: F401,E501


class IssueTokenRequest(object):
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
        'issue_address': 'str',
        'amount': 'float',
        'divisibility': 'float',
        'fee': 'float',
        'reissuable': 'bool',
        'flags': 'IssueTokenRequestFlags',
        'metadata': 'IssueTokenRequestMetadata'
    }

    attribute_map = {
        'issue_address': 'issueAddress',
        'amount': 'amount',
        'divisibility': 'divisibility',
        'fee': 'fee',
        'reissuable': 'reissuable',
        'flags': 'flags',
        'metadata': 'metadata'
    }

    def __init__(self, issue_address=None, amount=None, divisibility=None, fee=None, reissuable=None, flags=None, metadata=None):  # noqa: E501
        """IssueTokenRequest - a model defined in Swagger"""  # noqa: E501

        self._issue_address = None
        self._amount = None
        self._divisibility = None
        self._fee = None
        self._reissuable = None
        self._flags = None
        self._metadata = None
        self.discriminator = None

        self.issue_address = issue_address
        self.amount = amount
        self.divisibility = divisibility
        self.fee = fee
        self.reissuable = reissuable
        if flags is not None:
            self.flags = flags
        if metadata is not None:
            self.metadata = metadata

    @property
    def issue_address(self):
        """Gets the issue_address of this IssueTokenRequest.  # noqa: E501

        Address issuing the token  # noqa: E501

        :return: The issue_address of this IssueTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._issue_address

    @issue_address.setter
    def issue_address(self, issue_address):
        """Sets the issue_address of this IssueTokenRequest.

        Address issuing the token  # noqa: E501

        :param issue_address: The issue_address of this IssueTokenRequest.  # noqa: E501
        :type: str
        """
        if issue_address is None:
            raise ValueError("Invalid value for `issue_address`, must not be `None`")  # noqa: E501

        self._issue_address = issue_address

    @property
    def amount(self):
        """Gets the amount of this IssueTokenRequest.  # noqa: E501

        Number of tokens to issue  # noqa: E501

        :return: The amount of this IssueTokenRequest.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this IssueTokenRequest.

        Number of tokens to issue  # noqa: E501

        :param amount: The amount of this IssueTokenRequest.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def divisibility(self):
        """Gets the divisibility of this IssueTokenRequest.  # noqa: E501

        Number of decimal places the token should be divisble by (0-7)  # noqa: E501

        :return: The divisibility of this IssueTokenRequest.  # noqa: E501
        :rtype: float
        """
        return self._divisibility

    @divisibility.setter
    def divisibility(self, divisibility):
        """Sets the divisibility of this IssueTokenRequest.

        Number of decimal places the token should be divisble by (0-7)  # noqa: E501

        :param divisibility: The divisibility of this IssueTokenRequest.  # noqa: E501
        :type: float
        """
        if divisibility is None:
            raise ValueError("Invalid value for `divisibility`, must not be `None`")  # noqa: E501

        self._divisibility = divisibility

    @property
    def fee(self):
        """Gets the fee of this IssueTokenRequest.  # noqa: E501

        Fee in satoshi to include in the issuance transaction min 1000000000 (10 NEBL)  # noqa: E501

        :return: The fee of this IssueTokenRequest.  # noqa: E501
        :rtype: float
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this IssueTokenRequest.

        Fee in satoshi to include in the issuance transaction min 1000000000 (10 NEBL)  # noqa: E501

        :param fee: The fee of this IssueTokenRequest.  # noqa: E501
        :type: float
        """
        if fee is None:
            raise ValueError("Invalid value for `fee`, must not be `None`")  # noqa: E501

        self._fee = fee

    @property
    def reissuable(self):
        """Gets the reissuable of this IssueTokenRequest.  # noqa: E501

        whether the token should be reissuable  # noqa: E501

        :return: The reissuable of this IssueTokenRequest.  # noqa: E501
        :rtype: bool
        """
        return self._reissuable

    @reissuable.setter
    def reissuable(self, reissuable):
        """Sets the reissuable of this IssueTokenRequest.

        whether the token should be reissuable  # noqa: E501

        :param reissuable: The reissuable of this IssueTokenRequest.  # noqa: E501
        :type: bool
        """
        if reissuable is None:
            raise ValueError("Invalid value for `reissuable`, must not be `None`")  # noqa: E501

        self._reissuable = reissuable

    @property
    def flags(self):
        """Gets the flags of this IssueTokenRequest.  # noqa: E501


        :return: The flags of this IssueTokenRequest.  # noqa: E501
        :rtype: IssueTokenRequestFlags
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this IssueTokenRequest.


        :param flags: The flags of this IssueTokenRequest.  # noqa: E501
        :type: IssueTokenRequestFlags
        """

        self._flags = flags

    @property
    def metadata(self):
        """Gets the metadata of this IssueTokenRequest.  # noqa: E501


        :return: The metadata of this IssueTokenRequest.  # noqa: E501
        :rtype: IssueTokenRequestMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IssueTokenRequest.


        :param metadata: The metadata of this IssueTokenRequest.  # noqa: E501
        :type: IssueTokenRequestMetadata
        """

        self._metadata = metadata

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
        if not isinstance(other, IssueTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
