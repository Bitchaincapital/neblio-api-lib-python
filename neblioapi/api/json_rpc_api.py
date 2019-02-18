# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.2.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from neblioapi.api_client import ApiClient


class JSONRPCApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def r_pc(self, rpc_request, **kwargs):  # noqa: E501
        """Send a JSON-RPC call to a localhost neblio-Qt or nebliod node  # noqa: E501

        Call any Neblio RPC command from the Neblio API libraries. Useful for signing transactions with a local node and other functions. Will not work from this page due to CORS restrictions. Requires a node to be running locally at 127.0.0.1 - Use port 16326 for testnet.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.r_pc(rpc_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RpcRequest rpc_request: (required)
        :return: RpcResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.r_pc_with_http_info(rpc_request, **kwargs)  # noqa: E501
        else:
            (data) = self.r_pc_with_http_info(rpc_request, **kwargs)  # noqa: E501
            return data

    def r_pc_with_http_info(self, rpc_request, **kwargs):  # noqa: E501
        """Send a JSON-RPC call to a localhost neblio-Qt or nebliod node  # noqa: E501

        Call any Neblio RPC command from the Neblio API libraries. Useful for signing transactions with a local node and other functions. Will not work from this page due to CORS restrictions. Requires a node to be running locally at 127.0.0.1 - Use port 16326 for testnet.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.r_pc_with_http_info(rpc_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RpcRequest rpc_request: (required)
        :return: RpcResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_hosts = ['http://127.0.0.1:{port}']  # noqa: E501
        local_var_host = local_var_hosts[0]
        if kwargs.get('_host_index'):
            if int(kwags.get('_host_index')) < 0 or int(kawgs.get('_host_index')) >= len(local_var_hosts):
                raise ValueError("Invalid host index. Must be 0 <= index < %s" % len(local_var_host))
            local_var_host = local_var_hosts[int(kwargs.get('_host_index'))]
        local_var_params = locals()

        all_params = ['rpc_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params and key != "_host_index":
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method r_pc" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rpc_request' is set
        if ('rpc_request' not in local_var_params or
                local_var_params['rpc_request'] is None):
            raise ValueError("Missing the required parameter `rpc_request` when calling `r_pc`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'rpc_request' in local_var_params:
            body_params = local_var_params['rpc_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['rpcAuth']  # noqa: E501

        return self.api_client.call_api(
            '/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RpcResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            _host=local_var_host,
            collection_formats=collection_formats)