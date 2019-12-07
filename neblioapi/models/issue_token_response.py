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


class IssueTokenResponse(object):
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
        'token_id': 'str',
        'tx_hex': 'str'
    }

    attribute_map = {
        'token_id': 'tokenId',
        'tx_hex': 'txHex'
    }

    def __init__(self, token_id=None, tx_hex=None):  # noqa: E501
        """IssueTokenResponse - a model defined in OpenAPI"""  # noqa: E501

        self._token_id = None
        self._tx_hex = None
        self.discriminator = None

        if token_id is not None:
            self.token_id = token_id
        if tx_hex is not None:
            self.tx_hex = tx_hex

    @property
    def token_id(self):
        """Gets the token_id of this IssueTokenResponse.  # noqa: E501

        TokenId of the to be issued token  # noqa: E501

        :return: The token_id of this IssueTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this IssueTokenResponse.

        TokenId of the to be issued token  # noqa: E501

        :param token_id: The token_id of this IssueTokenResponse.  # noqa: E501
        :type: str
        """

        self._token_id = token_id

    @property
    def tx_hex(self):
        """Gets the tx_hex of this IssueTokenResponse.  # noqa: E501

        Unsigned, raw transaction hex of the transaction to issue the token  # noqa: E501

        :return: The tx_hex of this IssueTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._tx_hex

    @tx_hex.setter
    def tx_hex(self, tx_hex):
        """Sets the tx_hex of this IssueTokenResponse.

        Unsigned, raw transaction hex of the transaction to issue the token  # noqa: E501

        :param tx_hex: The tx_hex of this IssueTokenResponse.  # noqa: E501
        :type: str
        """

        self._tx_hex = tx_hex

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
        if not isinstance(other, IssueTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
