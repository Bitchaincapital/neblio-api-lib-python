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


class RpcResponse(object):
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
        'result': 'object',
        'id': 'str',
        'error': 'object'
    }

    attribute_map = {
        'result': 'result',
        'id': 'id',
        'error': 'error'
    }

    def __init__(self, result=None, id=None, error=None):  # noqa: E501
        """RpcResponse - a model defined in OpenAPI"""  # noqa: E501

        self._result = None
        self._id = None
        self._error = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if id is not None:
            self.id = id
        if error is not None:
            self.error = error

    @property
    def result(self):
        """Gets the result of this RpcResponse.  # noqa: E501

        Object containing the response output.  # noqa: E501

        :return: The result of this RpcResponse.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this RpcResponse.

        Object containing the response output.  # noqa: E501

        :param result: The result of this RpcResponse.  # noqa: E501
        :type: object
        """

        self._result = result

    @property
    def id(self):
        """Gets the id of this RpcResponse.  # noqa: E501

        Identifier of RCP caller  # noqa: E501

        :return: The id of this RpcResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RpcResponse.

        Identifier of RCP caller  # noqa: E501

        :param id: The id of this RpcResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def error(self):
        """Gets the error of this RpcResponse.  # noqa: E501

        Object containing any error information.  # noqa: E501

        :return: The error of this RpcResponse.  # noqa: E501
        :rtype: object
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this RpcResponse.

        Object containing any error information.  # noqa: E501

        :param error: The error of this RpcResponse.  # noqa: E501
        :type: object
        """

        self._error = error

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
        if not isinstance(other, RpcResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
