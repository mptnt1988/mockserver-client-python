# coding: utf-8

"""
    Mock Server API

    MockServer enables easy mocking of any system you integrate with via HTTP or HTTPS with clients written in Java, JavaScript and Ruby and a simple REST API (as shown below).  MockServer Proxy is a proxy that introspects all proxied traffic including encrypted SSL traffic and supports Port Forwarding, Web Proxying (i.e. HTTP proxy), HTTPS Tunneling Proxying (using HTTP CONNECT) and SOCKS Proxying (i.e. dynamic port forwarding).  Both MockServer and the MockServer Proxy record all received requests so that it is possible to verify exactly what requests have been sent by the system under test.  # noqa: E501

    OpenAPI spec version: 5.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class TimeToLive(object):
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
        'time_unit': 'str',
        'time_to_live': 'int',
        'unlimited': 'bool'
    }

    attribute_map = {
        'time_unit': 'timeUnit',
        'time_to_live': 'timeToLive',
        'unlimited': 'unlimited'
    }

    def __init__(self, time_unit=None, time_to_live=None, unlimited=None):  # noqa: E501
        """TimeToLive - a model defined in OpenAPI"""  # noqa: E501

        self._time_unit = None
        self._time_to_live = None
        self._unlimited = None
        self.discriminator = None

        if time_unit is not None:
            self.time_unit = time_unit
        if time_to_live is not None:
            self.time_to_live = time_to_live
        if unlimited is not None:
            self.unlimited = unlimited

    @property
    def time_unit(self):
        """Gets the time_unit of this TimeToLive.  # noqa: E501


        :return: The time_unit of this TimeToLive.  # noqa: E501
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this TimeToLive.


        :param time_unit: The time_unit of this TimeToLive.  # noqa: E501
        :type: str
        """
        allowed_values = ["HOURS", "MINUTES", "SECONDS", "MILLISECONDS", "MICROSECONDS", "NANOSECONDS"]  # noqa: E501
        if time_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `time_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(time_unit, allowed_values)
            )

        self._time_unit = time_unit

    @property
    def time_to_live(self):
        """Gets the time_to_live of this TimeToLive.  # noqa: E501


        :return: The time_to_live of this TimeToLive.  # noqa: E501
        :rtype: int
        """
        return self._time_to_live

    @time_to_live.setter
    def time_to_live(self, time_to_live):
        """Sets the time_to_live of this TimeToLive.


        :param time_to_live: The time_to_live of this TimeToLive.  # noqa: E501
        :type: int
        """

        self._time_to_live = time_to_live

    @property
    def unlimited(self):
        """Gets the unlimited of this TimeToLive.  # noqa: E501


        :return: The unlimited of this TimeToLive.  # noqa: E501
        :rtype: bool
        """
        return self._unlimited

    @unlimited.setter
    def unlimited(self, unlimited):
        """Sets the unlimited of this TimeToLive.


        :param unlimited: The unlimited of this TimeToLive.  # noqa: E501
        :type: bool
        """

        self._unlimited = unlimited

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
        if not isinstance(other, TimeToLive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
