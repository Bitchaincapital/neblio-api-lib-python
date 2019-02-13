# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.2.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BurnTokenRequest(object):
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
        'fee': 'float',
        '_from': 'list[str]',
        'transfer': 'list[SendTokenRequestTo]',
        'burn': 'list[BurnTokenRequestBurn]'
    }

    attribute_map = {
        'fee': 'fee',
        '_from': 'from',
        'transfer': 'transfer',
        'burn': 'burn'
    }

    def __init__(self, fee=None, _from=None, transfer=None, burn=None):  # noqa: E501
        """BurnTokenRequest - a model defined in OpenAPI"""  # noqa: E501

        self._fee = None
        self.__from = None
        self._transfer = None
        self._burn = None
        self.discriminator = None

        self.fee = fee
        if _from is not None:
            self._from = _from
        if transfer is not None:
            self.transfer = transfer
        self.burn = burn

    @property
    def fee(self):
        """Gets the fee of this BurnTokenRequest.  # noqa: E501

        Fee in satoshi to include in the issuance transaction min 10000 (0.0001 NEBL)  # noqa: E501

        :return: The fee of this BurnTokenRequest.  # noqa: E501
        :rtype: float
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this BurnTokenRequest.

        Fee in satoshi to include in the issuance transaction min 10000 (0.0001 NEBL)  # noqa: E501

        :param fee: The fee of this BurnTokenRequest.  # noqa: E501
        :type: float
        """
        if fee is None:
            raise ValueError("Invalid value for `fee`, must not be `None`")  # noqa: E501

        self._fee = fee

    @property
    def _from(self):
        """Gets the _from of this BurnTokenRequest.  # noqa: E501

        Array of addresses to send the token from  # noqa: E501

        :return: The _from of this BurnTokenRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this BurnTokenRequest.

        Array of addresses to send the token from  # noqa: E501

        :param _from: The _from of this BurnTokenRequest.  # noqa: E501
        :type: list[str]
        """

        self.__from = _from

    @property
    def transfer(self):
        """Gets the transfer of this BurnTokenRequest.  # noqa: E501


        :return: The transfer of this BurnTokenRequest.  # noqa: E501
        :rtype: list[SendTokenRequestTo]
        """
        return self._transfer

    @transfer.setter
    def transfer(self, transfer):
        """Sets the transfer of this BurnTokenRequest.


        :param transfer: The transfer of this BurnTokenRequest.  # noqa: E501
        :type: list[SendTokenRequestTo]
        """

        self._transfer = transfer

    @property
    def burn(self):
        """Gets the burn of this BurnTokenRequest.  # noqa: E501

        Array of objects representing tokens to be burned  # noqa: E501

        :return: The burn of this BurnTokenRequest.  # noqa: E501
        :rtype: list[BurnTokenRequestBurn]
        """
        return self._burn

    @burn.setter
    def burn(self, burn):
        """Sets the burn of this BurnTokenRequest.

        Array of objects representing tokens to be burned  # noqa: E501

        :param burn: The burn of this BurnTokenRequest.  # noqa: E501
        :type: list[BurnTokenRequestBurn]
        """
        if burn is None:
            raise ValueError("Invalid value for `burn`, must not be `None`")  # noqa: E501

        self._burn = burn

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
        if not isinstance(other, BurnTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
