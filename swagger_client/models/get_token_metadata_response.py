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

from swagger_client.models.get_token_metadata_response_metadata_of_issuance import GetTokenMetadataResponseMetadataOfIssuance  # noqa: F401,E501


class GetTokenMetadataResponse(object):
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
        'divisibility': 'float',
        'lock_status': 'bool',
        'aggregation_policy': 'str',
        'total_supply': 'float',
        'num_of_holders': 'float',
        'num_of_transfers': 'float',
        'numof_issuance': 'float',
        'num_of_burns': 'float',
        'first_block': 'float',
        'issuance_txid': 'str',
        'issue_address': 'str',
        'metadata_of_issuance': 'GetTokenMetadataResponseMetadataOfIssuance',
        'metadata_of_utxo': 'GetTokenMetadataResponseMetadataOfIssuance'
    }

    attribute_map = {
        'token_id': 'tokenId',
        'divisibility': 'divisibility',
        'lock_status': 'lockStatus',
        'aggregation_policy': 'aggregationPolicy',
        'total_supply': 'totalSupply',
        'num_of_holders': 'numOfHolders',
        'num_of_transfers': 'numOfTransfers',
        'numof_issuance': 'numofIssuance',
        'num_of_burns': 'numOfBurns',
        'first_block': 'firstBlock',
        'issuance_txid': 'issuanceTxid',
        'issue_address': 'issueAddress',
        'metadata_of_issuance': 'metadataOfIssuance',
        'metadata_of_utxo': 'metadataOfUtxo'
    }

    def __init__(self, token_id=None, divisibility=None, lock_status=None, aggregation_policy=None, total_supply=None, num_of_holders=None, num_of_transfers=None, numof_issuance=None, num_of_burns=None, first_block=None, issuance_txid=None, issue_address=None, metadata_of_issuance=None, metadata_of_utxo=None):  # noqa: E501
        """GetTokenMetadataResponse - a model defined in Swagger"""  # noqa: E501

        self._token_id = None
        self._divisibility = None
        self._lock_status = None
        self._aggregation_policy = None
        self._total_supply = None
        self._num_of_holders = None
        self._num_of_transfers = None
        self._numof_issuance = None
        self._num_of_burns = None
        self._first_block = None
        self._issuance_txid = None
        self._issue_address = None
        self._metadata_of_issuance = None
        self._metadata_of_utxo = None
        self.discriminator = None

        if token_id is not None:
            self.token_id = token_id
        if divisibility is not None:
            self.divisibility = divisibility
        if lock_status is not None:
            self.lock_status = lock_status
        if aggregation_policy is not None:
            self.aggregation_policy = aggregation_policy
        if total_supply is not None:
            self.total_supply = total_supply
        if num_of_holders is not None:
            self.num_of_holders = num_of_holders
        if num_of_transfers is not None:
            self.num_of_transfers = num_of_transfers
        if numof_issuance is not None:
            self.numof_issuance = numof_issuance
        if num_of_burns is not None:
            self.num_of_burns = num_of_burns
        if first_block is not None:
            self.first_block = first_block
        if issuance_txid is not None:
            self.issuance_txid = issuance_txid
        if issue_address is not None:
            self.issue_address = issue_address
        if metadata_of_issuance is not None:
            self.metadata_of_issuance = metadata_of_issuance
        if metadata_of_utxo is not None:
            self.metadata_of_utxo = metadata_of_utxo

    @property
    def token_id(self):
        """Gets the token_id of this GetTokenMetadataResponse.  # noqa: E501

        ID of the token  # noqa: E501

        :return: The token_id of this GetTokenMetadataResponse.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this GetTokenMetadataResponse.

        ID of the token  # noqa: E501

        :param token_id: The token_id of this GetTokenMetadataResponse.  # noqa: E501
        :type: str
        """

        self._token_id = token_id

    @property
    def divisibility(self):
        """Gets the divisibility of this GetTokenMetadataResponse.  # noqa: E501

        Decimal places the token is divisible to  # noqa: E501

        :return: The divisibility of this GetTokenMetadataResponse.  # noqa: E501
        :rtype: float
        """
        return self._divisibility

    @divisibility.setter
    def divisibility(self, divisibility):
        """Sets the divisibility of this GetTokenMetadataResponse.

        Decimal places the token is divisible to  # noqa: E501

        :param divisibility: The divisibility of this GetTokenMetadataResponse.  # noqa: E501
        :type: float
        """

        self._divisibility = divisibility

    @property
    def lock_status(self):
        """Gets the lock_status of this GetTokenMetadataResponse.  # noqa: E501

        Whether issuance of more tokens is locked  # noqa: E501

        :return: The lock_status of this GetTokenMetadataResponse.  # noqa: E501
        :rtype: bool
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        """Sets the lock_status of this GetTokenMetadataResponse.

        Whether issuance of more tokens is locked  # noqa: E501

        :param lock_status: The lock_status of this GetTokenMetadataResponse.  # noqa: E501
        :type: bool
        """

        self._lock_status = lock_status

    @property
    def aggregation_policy(self):
        """Gets the aggregation_policy of this GetTokenMetadataResponse.  # noqa: E501

        Whether the tokens are aggregatable  # noqa: E501

        :return: The aggregation_policy of this GetTokenMetadataResponse.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_policy

    @aggregation_policy.setter
    def aggregation_policy(self, aggregation_policy):
        """Sets the aggregation_policy of this GetTokenMetadataResponse.

        Whether the tokens are aggregatable  # noqa: E501

        :param aggregation_policy: The aggregation_policy of this GetTokenMetadataResponse.  # noqa: E501
        :type: str
        """

        self._aggregation_policy = aggregation_policy

    @property
    def total_supply(self):
        """Gets the total_supply of this GetTokenMetadataResponse.  # noqa: E501

        Total number of tokens in supply  # noqa: E501

        :return: The total_supply of this GetTokenMetadataResponse.  # noqa: E501
        :rtype: float
        """
        return self._total_supply

    @total_supply.setter
    def total_supply(self, total_supply):
        """Sets the total_supply of this GetTokenMetadataResponse.

        Total number of tokens in supply  # noqa: E501

        :param total_supply: The total_supply of this GetTokenMetadataResponse.  # noqa: E501
        :type: float
        """

        self._total_supply = total_supply

    @property
    def num_of_holders(self):
        """Gets the num_of_holders of this GetTokenMetadataResponse.  # noqa: E501

        Total number of addresses this token is held at  # noqa: E501

        :return: The num_of_holders of this GetTokenMetadataResponse.  # noqa: E501
        :rtype: float
        """
        return self._num_of_holders

    @num_of_holders.setter
    def num_of_holders(self, num_of_holders):
        """Sets the num_of_holders of this GetTokenMetadataResponse.

        Total number of addresses this token is held at  # noqa: E501

        :param num_of_holders: The num_of_holders of this GetTokenMetadataResponse.  # noqa: E501
        :type: float
        """

        self._num_of_holders = num_of_holders

    @property
    def num_of_transfers(self):
        """Gets the num_of_transfers of this GetTokenMetadataResponse.  # noqa: E501

        Total number of transactions of this token  # noqa: E501

        :return: The num_of_transfers of this GetTokenMetadataResponse.  # noqa: E501
        :rtype: float
        """
        return self._num_of_transfers

    @num_of_transfers.setter
    def num_of_transfers(self, num_of_transfers):
        """Sets the num_of_transfers of this GetTokenMetadataResponse.

        Total number of transactions of this token  # noqa: E501

        :param num_of_transfers: The num_of_transfers of this GetTokenMetadataResponse.  # noqa: E501
        :type: float
        """

        self._num_of_transfers = num_of_transfers

    @property
    def numof_issuance(self):
        """Gets the numof_issuance of this GetTokenMetadataResponse.  # noqa: E501

        Total number of times this token has been issued  # noqa: E501

        :return: The numof_issuance of this GetTokenMetadataResponse.  # noqa: E501
        :rtype: float
        """
        return self._numof_issuance

    @numof_issuance.setter
    def numof_issuance(self, numof_issuance):
        """Sets the numof_issuance of this GetTokenMetadataResponse.

        Total number of times this token has been issued  # noqa: E501

        :param numof_issuance: The numof_issuance of this GetTokenMetadataResponse.  # noqa: E501
        :type: float
        """

        self._numof_issuance = numof_issuance

    @property
    def num_of_burns(self):
        """Gets the num_of_burns of this GetTokenMetadataResponse.  # noqa: E501

        Number of times tokens have been burned  # noqa: E501

        :return: The num_of_burns of this GetTokenMetadataResponse.  # noqa: E501
        :rtype: float
        """
        return self._num_of_burns

    @num_of_burns.setter
    def num_of_burns(self, num_of_burns):
        """Sets the num_of_burns of this GetTokenMetadataResponse.

        Number of times tokens have been burned  # noqa: E501

        :param num_of_burns: The num_of_burns of this GetTokenMetadataResponse.  # noqa: E501
        :type: float
        """

        self._num_of_burns = num_of_burns

    @property
    def first_block(self):
        """Gets the first_block of this GetTokenMetadataResponse.  # noqa: E501

        Block number token was issued in  # noqa: E501

        :return: The first_block of this GetTokenMetadataResponse.  # noqa: E501
        :rtype: float
        """
        return self._first_block

    @first_block.setter
    def first_block(self, first_block):
        """Sets the first_block of this GetTokenMetadataResponse.

        Block number token was issued in  # noqa: E501

        :param first_block: The first_block of this GetTokenMetadataResponse.  # noqa: E501
        :type: float
        """

        self._first_block = first_block

    @property
    def issuance_txid(self):
        """Gets the issuance_txid of this GetTokenMetadataResponse.  # noqa: E501

        TXID the token was issued with  # noqa: E501

        :return: The issuance_txid of this GetTokenMetadataResponse.  # noqa: E501
        :rtype: str
        """
        return self._issuance_txid

    @issuance_txid.setter
    def issuance_txid(self, issuance_txid):
        """Sets the issuance_txid of this GetTokenMetadataResponse.

        TXID the token was issued with  # noqa: E501

        :param issuance_txid: The issuance_txid of this GetTokenMetadataResponse.  # noqa: E501
        :type: str
        """

        self._issuance_txid = issuance_txid

    @property
    def issue_address(self):
        """Gets the issue_address of this GetTokenMetadataResponse.  # noqa: E501

        Address that issued the tokens  # noqa: E501

        :return: The issue_address of this GetTokenMetadataResponse.  # noqa: E501
        :rtype: str
        """
        return self._issue_address

    @issue_address.setter
    def issue_address(self, issue_address):
        """Sets the issue_address of this GetTokenMetadataResponse.

        Address that issued the tokens  # noqa: E501

        :param issue_address: The issue_address of this GetTokenMetadataResponse.  # noqa: E501
        :type: str
        """

        self._issue_address = issue_address

    @property
    def metadata_of_issuance(self):
        """Gets the metadata_of_issuance of this GetTokenMetadataResponse.  # noqa: E501


        :return: The metadata_of_issuance of this GetTokenMetadataResponse.  # noqa: E501
        :rtype: GetTokenMetadataResponseMetadataOfIssuance
        """
        return self._metadata_of_issuance

    @metadata_of_issuance.setter
    def metadata_of_issuance(self, metadata_of_issuance):
        """Sets the metadata_of_issuance of this GetTokenMetadataResponse.


        :param metadata_of_issuance: The metadata_of_issuance of this GetTokenMetadataResponse.  # noqa: E501
        :type: GetTokenMetadataResponseMetadataOfIssuance
        """

        self._metadata_of_issuance = metadata_of_issuance

    @property
    def metadata_of_utxo(self):
        """Gets the metadata_of_utxo of this GetTokenMetadataResponse.  # noqa: E501


        :return: The metadata_of_utxo of this GetTokenMetadataResponse.  # noqa: E501
        :rtype: GetTokenMetadataResponseMetadataOfIssuance
        """
        return self._metadata_of_utxo

    @metadata_of_utxo.setter
    def metadata_of_utxo(self, metadata_of_utxo):
        """Sets the metadata_of_utxo of this GetTokenMetadataResponse.


        :param metadata_of_utxo: The metadata_of_utxo of this GetTokenMetadataResponse.  # noqa: E501
        :type: GetTokenMetadataResponseMetadataOfIssuance
        """

        self._metadata_of_utxo = metadata_of_utxo

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
        if not isinstance(other, GetTokenMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
