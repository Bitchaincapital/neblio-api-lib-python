# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.3.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from neblioapi.api_client import ApiClient


class TestnetFaucetApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def testnet_get_faucet(self, address, **kwargs):  # noqa: E501
        """Withdraws testnet NEBL to the specified address  # noqa: E501

        Withdraw testnet NEBL to your Neblio Testnet address. By default amount is 1500000000 or 15 NEBL and has a max of 50 NEBL. Only 2 withdrawals allowed per 24 hour period.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.testnet_get_faucet(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Your Neblio Testnet Address (required)
        :param float amount: Amount of NEBL to withdrawal in satoshis
        :return: GetFaucetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.testnet_get_faucet_with_http_info(address, **kwargs)  # noqa: E501
        else:
            (data) = self.testnet_get_faucet_with_http_info(address, **kwargs)  # noqa: E501
            return data

    def testnet_get_faucet_with_http_info(self, address, **kwargs):  # noqa: E501
        """Withdraws testnet NEBL to the specified address  # noqa: E501

        Withdraw testnet NEBL to your Neblio Testnet address. By default amount is 1500000000 or 15 NEBL and has a max of 50 NEBL. Only 2 withdrawals allowed per 24 hour period.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.testnet_get_faucet_with_http_info(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Your Neblio Testnet Address (required)
        :param float amount: Amount of NEBL to withdrawal in satoshis
        :return: GetFaucetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['address', 'amount']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method testnet_get_faucet" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in local_var_params or
                local_var_params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `testnet_get_faucet`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))  # noqa: E501
        if 'amount' in local_var_params:
            query_params.append(('amount', local_var_params['amount']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/testnet/faucet', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetFaucetResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
