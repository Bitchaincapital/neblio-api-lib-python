# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.testnet_insight_api import TestnetInsightApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTestnetInsightApi(unittest.TestCase):
    """TestnetInsightApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.testnet_insight_api.TestnetInsightApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_testnet_get_address(self):
        """Test case for testnet_get_address

        Returns address object  # noqa: E501
        """
        pass

    def test_testnet_get_address_balance(self):
        """Test case for testnet_get_address_balance

        Returns address balance in sats  # noqa: E501
        """
        pass

    def test_testnet_get_address_total_received(self):
        """Test case for testnet_get_address_total_received

        Returns total received by address in sats  # noqa: E501
        """
        pass

    def test_testnet_get_address_total_sent(self):
        """Test case for testnet_get_address_total_sent

        Returns total sent by address in sats  # noqa: E501
        """
        pass

    def test_testnet_get_address_unconfirmed_balance(self):
        """Test case for testnet_get_address_unconfirmed_balance

        Returns address unconfirmed balance in sats  # noqa: E501
        """
        pass

    def test_testnet_get_address_utxos(self):
        """Test case for testnet_get_address_utxos

        Returns all UTXOs at a given address  # noqa: E501
        """
        pass

    def test_testnet_get_block(self):
        """Test case for testnet_get_block

        Returns information regarding a Neblio block  # noqa: E501
        """
        pass

    def test_testnet_get_block_index(self):
        """Test case for testnet_get_block_index

        Returns block hash of block  # noqa: E501
        """
        pass

    def test_testnet_get_raw_tx(self):
        """Test case for testnet_get_raw_tx

        Returns raw transaction hex  # noqa: E501
        """
        pass

    def test_testnet_get_status(self):
        """Test case for testnet_get_status

        Utility API for calling several blockchain node functions  # noqa: E501
        """
        pass

    def test_testnet_get_sync(self):
        """Test case for testnet_get_sync

        Get node sync status  # noqa: E501
        """
        pass

    def test_testnet_get_tx(self):
        """Test case for testnet_get_tx

        Returns transaction object  # noqa: E501
        """
        pass

    def test_testnet_get_txs(self):
        """Test case for testnet_get_txs

        Get transactions by block or address  # noqa: E501
        """
        pass

    def test_testnet_send_tx(self):
        """Test case for testnet_send_tx

        Broadcasts a signed raw transaction to the network (not NTP1 specific)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
