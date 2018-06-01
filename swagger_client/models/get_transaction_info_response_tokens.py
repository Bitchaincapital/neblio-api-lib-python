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


class GetTransactionInfoResponseTokens(object):
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
        'token_id': 'str',
        'amount': 'float',
        'issue_txid': 'str',
        'divisibility': 'float',
        'lock_status': 'bool',
        'aggregation_policy': 'str'
    }

    attribute_map = {
        'token_id': 'tokenId',
        'amount': 'amount',
        'issue_txid': 'issueTxid',
        'divisibility': 'divisibility',
        'lock_status': 'lockStatus',
        'aggregation_policy': 'aggregationPolicy'
    }

    def __init__(self, token_id=None, amount=None, issue_txid=None, divisibility=None, lock_status=None, aggregation_policy=None):  # noqa: E501
        """GetTransactionInfoResponseTokens - a model defined in Swagger"""  # noqa: E501

        self._token_id = None
        self._amount = None
        self._issue_txid = None
        self._divisibility = None
        self._lock_status = None
        self._aggregation_policy = None
        self.discriminator = None

        if token_id is not None:
            self.token_id = token_id
        if amount is not None:
            self.amount = amount
        if issue_txid is not None:
            self.issue_txid = issue_txid
        if divisibility is not None:
            self.divisibility = divisibility
        if lock_status is not None:
            self.lock_status = lock_status
        if aggregation_policy is not None:
            self.aggregation_policy = aggregation_policy

    @property
    def token_id(self):
        """Gets the token_id of this GetTransactionInfoResponseTokens.  # noqa: E501

        ID of the token  # noqa: E501

        :return: The token_id of this GetTransactionInfoResponseTokens.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this GetTransactionInfoResponseTokens.

        ID of the token  # noqa: E501

        :param token_id: The token_id of this GetTransactionInfoResponseTokens.  # noqa: E501
        :type: str
        """

        self._token_id = token_id

    @property
    def amount(self):
        """Gets the amount of this GetTransactionInfoResponseTokens.  # noqa: E501

        Number of tokens  # noqa: E501

        :return: The amount of this GetTransactionInfoResponseTokens.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetTransactionInfoResponseTokens.

        Number of tokens  # noqa: E501

        :param amount: The amount of this GetTransactionInfoResponseTokens.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def issue_txid(self):
        """Gets the issue_txid of this GetTransactionInfoResponseTokens.  # noqa: E501

        TXID the token was issued in  # noqa: E501

        :return: The issue_txid of this GetTransactionInfoResponseTokens.  # noqa: E501
        :rtype: str
        """
        return self._issue_txid

    @issue_txid.setter
    def issue_txid(self, issue_txid):
        """Sets the issue_txid of this GetTransactionInfoResponseTokens.

        TXID the token was issued in  # noqa: E501

        :param issue_txid: The issue_txid of this GetTransactionInfoResponseTokens.  # noqa: E501
        :type: str
        """

        self._issue_txid = issue_txid

    @property
    def divisibility(self):
        """Gets the divisibility of this GetTransactionInfoResponseTokens.  # noqa: E501

        Decimal places the token is divisible to  # noqa: E501

        :return: The divisibility of this GetTransactionInfoResponseTokens.  # noqa: E501
        :rtype: float
        """
        return self._divisibility

    @divisibility.setter
    def divisibility(self, divisibility):
        """Sets the divisibility of this GetTransactionInfoResponseTokens.

        Decimal places the token is divisible to  # noqa: E501

        :param divisibility: The divisibility of this GetTransactionInfoResponseTokens.  # noqa: E501
        :type: float
        """

        self._divisibility = divisibility

    @property
    def lock_status(self):
        """Gets the lock_status of this GetTransactionInfoResponseTokens.  # noqa: E501

        Whether issuance of more tokens is locked  # noqa: E501

        :return: The lock_status of this GetTransactionInfoResponseTokens.  # noqa: E501
        :rtype: bool
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        """Sets the lock_status of this GetTransactionInfoResponseTokens.

        Whether issuance of more tokens is locked  # noqa: E501

        :param lock_status: The lock_status of this GetTransactionInfoResponseTokens.  # noqa: E501
        :type: bool
        """

        self._lock_status = lock_status

    @property
    def aggregation_policy(self):
        """Gets the aggregation_policy of this GetTransactionInfoResponseTokens.  # noqa: E501

        Whether the tokens are aggregatable  # noqa: E501

        :return: The aggregation_policy of this GetTransactionInfoResponseTokens.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_policy

    @aggregation_policy.setter
    def aggregation_policy(self, aggregation_policy):
        """Sets the aggregation_policy of this GetTransactionInfoResponseTokens.

        Whether the tokens are aggregatable  # noqa: E501

        :param aggregation_policy: The aggregation_policy of this GetTransactionInfoResponseTokens.  # noqa: E501
        :type: str
        """

        self._aggregation_policy = aggregation_policy

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
        if not isinstance(other, GetTransactionInfoResponseTokens):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
