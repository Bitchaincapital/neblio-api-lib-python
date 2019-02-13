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


class GetAddressInfoResponseUtxos(object):
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
        'script_pub_key': 'object',
        'blocktime': 'float',
        'index': 'float',
        'txid': 'str',
        'tokens': 'list[GetAddressInfoResponseTokens]',
        'used': 'bool',
        'value': 'float',
        'blockheight': 'float'
    }

    attribute_map = {
        'script_pub_key': 'scriptPubKey',
        'blocktime': 'blocktime',
        'index': 'index',
        'txid': 'txid',
        'tokens': 'tokens',
        'used': 'used',
        'value': 'value',
        'blockheight': 'blockheight'
    }

    def __init__(self, script_pub_key=None, blocktime=None, index=None, txid=None, tokens=None, used=None, value=None, blockheight=None):  # noqa: E501
        """GetAddressInfoResponseUtxos - a model defined in OpenAPI"""  # noqa: E501

        self._script_pub_key = None
        self._blocktime = None
        self._index = None
        self._txid = None
        self._tokens = None
        self._used = None
        self._value = None
        self._blockheight = None
        self.discriminator = None

        if script_pub_key is not None:
            self.script_pub_key = script_pub_key
        if blocktime is not None:
            self.blocktime = blocktime
        if index is not None:
            self.index = index
        if txid is not None:
            self.txid = txid
        if tokens is not None:
            self.tokens = tokens
        if used is not None:
            self.used = used
        if value is not None:
            self.value = value
        if blockheight is not None:
            self.blockheight = blockheight

    @property
    def script_pub_key(self):
        """Gets the script_pub_key of this GetAddressInfoResponseUtxos.  # noqa: E501

        Object representing the scruptPubKey of the UTXO  # noqa: E501

        :return: The script_pub_key of this GetAddressInfoResponseUtxos.  # noqa: E501
        :rtype: object
        """
        return self._script_pub_key

    @script_pub_key.setter
    def script_pub_key(self, script_pub_key):
        """Sets the script_pub_key of this GetAddressInfoResponseUtxos.

        Object representing the scruptPubKey of the UTXO  # noqa: E501

        :param script_pub_key: The script_pub_key of this GetAddressInfoResponseUtxos.  # noqa: E501
        :type: object
        """

        self._script_pub_key = script_pub_key

    @property
    def blocktime(self):
        """Gets the blocktime of this GetAddressInfoResponseUtxos.  # noqa: E501

        Blocktime of the UTXO  # noqa: E501

        :return: The blocktime of this GetAddressInfoResponseUtxos.  # noqa: E501
        :rtype: float
        """
        return self._blocktime

    @blocktime.setter
    def blocktime(self, blocktime):
        """Sets the blocktime of this GetAddressInfoResponseUtxos.

        Blocktime of the UTXO  # noqa: E501

        :param blocktime: The blocktime of this GetAddressInfoResponseUtxos.  # noqa: E501
        :type: float
        """

        self._blocktime = blocktime

    @property
    def index(self):
        """Gets the index of this GetAddressInfoResponseUtxos.  # noqa: E501

        Index of the UTXO at this address  # noqa: E501

        :return: The index of this GetAddressInfoResponseUtxos.  # noqa: E501
        :rtype: float
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this GetAddressInfoResponseUtxos.

        Index of the UTXO at this address  # noqa: E501

        :param index: The index of this GetAddressInfoResponseUtxos.  # noqa: E501
        :type: float
        """

        self._index = index

    @property
    def txid(self):
        """Gets the txid of this GetAddressInfoResponseUtxos.  # noqa: E501

        Txid of this UTXO  # noqa: E501

        :return: The txid of this GetAddressInfoResponseUtxos.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this GetAddressInfoResponseUtxos.

        Txid of this UTXO  # noqa: E501

        :param txid: The txid of this GetAddressInfoResponseUtxos.  # noqa: E501
        :type: str
        """

        self._txid = txid

    @property
    def tokens(self):
        """Gets the tokens of this GetAddressInfoResponseUtxos.  # noqa: E501

        Array of NTP1 tokens in this UTXO.  # noqa: E501

        :return: The tokens of this GetAddressInfoResponseUtxos.  # noqa: E501
        :rtype: list[GetAddressInfoResponseTokens]
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """Sets the tokens of this GetAddressInfoResponseUtxos.

        Array of NTP1 tokens in this UTXO.  # noqa: E501

        :param tokens: The tokens of this GetAddressInfoResponseUtxos.  # noqa: E501
        :type: list[GetAddressInfoResponseTokens]
        """

        self._tokens = tokens

    @property
    def used(self):
        """Gets the used of this GetAddressInfoResponseUtxos.  # noqa: E501

        Whether the UTXO has been used  # noqa: E501

        :return: The used of this GetAddressInfoResponseUtxos.  # noqa: E501
        :rtype: bool
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this GetAddressInfoResponseUtxos.

        Whether the UTXO has been used  # noqa: E501

        :param used: The used of this GetAddressInfoResponseUtxos.  # noqa: E501
        :type: bool
        """

        self._used = used

    @property
    def value(self):
        """Gets the value of this GetAddressInfoResponseUtxos.  # noqa: E501

        Value of the UTXO in NEBL satoshi  # noqa: E501

        :return: The value of this GetAddressInfoResponseUtxos.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GetAddressInfoResponseUtxos.

        Value of the UTXO in NEBL satoshi  # noqa: E501

        :param value: The value of this GetAddressInfoResponseUtxos.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def blockheight(self):
        """Gets the blockheight of this GetAddressInfoResponseUtxos.  # noqa: E501

        Blockheight of the UTXO  # noqa: E501

        :return: The blockheight of this GetAddressInfoResponseUtxos.  # noqa: E501
        :rtype: float
        """
        return self._blockheight

    @blockheight.setter
    def blockheight(self, blockheight):
        """Sets the blockheight of this GetAddressInfoResponseUtxos.

        Blockheight of the UTXO  # noqa: E501

        :param blockheight: The blockheight of this GetAddressInfoResponseUtxos.  # noqa: E501
        :type: float
        """

        self._blockheight = blockheight

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
        if not isinstance(other, GetAddressInfoResponseUtxos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
