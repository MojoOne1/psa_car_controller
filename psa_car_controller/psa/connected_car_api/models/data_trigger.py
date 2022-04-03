# coding: utf-8

"""
    Groupe PSA Connected Car - WEB API B2C

    *PSA B2C Connected Car API*  # Introduction This is the description of the *Groupe PSA Connected Car V2 API*. The speccification is  is based on **OpenAPI Specification version 3** and can be displayed via [ReDoc](https://github.com/Rebilly/ReDoc)a or [Swagger](http://swagger.io).   This API allows applications to fetch data from the connected Vehicles data platform. # Authentication PSA Connected Car APIs uses the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) protocol for authentication and Authorization. any application require a valid [Access Token](https://tools.ietf.org/html/rfc6749#section-1.4) to access to user data. # Errors   Error codes returned by all REST APIs comply with the standard. Nevertheless, PSA Services (callers) need to have more complete data structures (even when the answer is not Http-OK) to better detail the type of error by providing application code, message and a debugging code(for investigation purposes). The http code of the response is managed by the protocol itself (in the header).      **Errors are  returned as a generic error response:**    * ```xError``` object model.       # noqa: E501

    OpenAPI spec version: 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DataTrigger(object):
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
        'data': 'str',
        'op': 'str',
        'value': 'list[str]'
    }

    attribute_map = {
        'data': 'data',
        'op': 'op',
        'value': 'value'
    }

    def __init__(self, data=None, op=None, value=None):  # noqa: E501
        """DataTrigger - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._op = None
        self._value = None
        self.discriminator = None

        self.data = data
        self.op = op
        if value is not None:
            self.value = value

    @property
    def data(self):
        """Gets the data of this DataTrigger.  # noqa: E501

        The left operand of the trigger function. The following Table details for each operand data its type, the supported operator and the possibly retruned value:  |**Data**|**Type**|**Op**|**Value**| |---|---| ---:| ---:| | Vehicle.alert | List of value | OnChange (at least one)/IncludedIn/EqualTo | Value (ObjetAlert) | | Vehicle.odometer | Integer | equalTo/greaterThan/lowerThan/ | Value | | vehicle.engines.running (boolean) | Boolean | OnChange/equalTo | Value (true/false) | | vehicle.engines.thermic.oil.temp | Integer | equalTo/greaterThan/ lowerThan/ | Value | | vehicle.energy.electric.level | Number | equalTo/greaterThan/ lowerThan/ | Value | | vehicle.energy.electric.autonomy | Number | equalTo/greaterThan/ lowerThan/ | Value | | vehicle.energy.fuel.level | Number | equalTo/greaterThan/ lowerThan/ | Value | | vehicle.energy.fuel.autonomy | Number | equalTo/greaterThan/ lowerThan/ | Value | | vehicle.autonomy (global) | Number | equalTo/greaterThan/ lowerThan/ | Value | | vehicle.energy.charging.status | Enum(ChargingStatusEnum) | OnChange/equalTo | Value | | vehicle.energy.charging.plugged | Boolean | OnChange/equalTo | Value | | vehicle.doorsState.lockedState | N/A | OnChange | Value | | vehicle.doorsState.opening | N/A | OnChange | Value | | vehicle.kinetic.moving| Boolean | OnChange/equalTo | Value (true/false) | | vehicle.kinetic.speed | Number | equalTo/greaterThan/ lowerThan/ | Value | | vehicle.trip| Literal | OnChange| Value(IDTRIP) | | vehicle.maintenance.daysBeforeMaintenance, | Number | OnChange/equalTo/ greaterThan/ lowerThan/ | Value | | vehicle.maintenance.mileageBeforeMaintenance| Number | OnChange/equalTo/ greaterThan/ lowerThan/ | Value | | vehicle.safety.beltWarning | Enum(beltWarning) | OnChange/equalTo | Value | | environment.air.temp | Number | equalTo/greaterThan/lowerThan/ | Value | | privacy.state | Enum(Privacy) | equalTo / OnChange/IncludedIN | Value |   # noqa: E501

        :return: The data of this DataTrigger.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DataTrigger.

        The left operand of the trigger function. The following Table details for each operand data its type, the supported operator and the possibly retruned value:  |**Data**|**Type**|**Op**|**Value**| |---|---| ---:| ---:| | Vehicle.alert | List of value | OnChange (at least one)/IncludedIn/EqualTo | Value (ObjetAlert) | | Vehicle.odometer | Integer | equalTo/greaterThan/lowerThan/ | Value | | vehicle.engines.running (boolean) | Boolean | OnChange/equalTo | Value (true/false) | | vehicle.engines.thermic.oil.temp | Integer | equalTo/greaterThan/ lowerThan/ | Value | | vehicle.energy.electric.level | Number | equalTo/greaterThan/ lowerThan/ | Value | | vehicle.energy.electric.autonomy | Number | equalTo/greaterThan/ lowerThan/ | Value | | vehicle.energy.fuel.level | Number | equalTo/greaterThan/ lowerThan/ | Value | | vehicle.energy.fuel.autonomy | Number | equalTo/greaterThan/ lowerThan/ | Value | | vehicle.autonomy (global) | Number | equalTo/greaterThan/ lowerThan/ | Value | | vehicle.energy.charging.status | Enum(ChargingStatusEnum) | OnChange/equalTo | Value | | vehicle.energy.charging.plugged | Boolean | OnChange/equalTo | Value | | vehicle.doorsState.lockedState | N/A | OnChange | Value | | vehicle.doorsState.opening | N/A | OnChange | Value | | vehicle.kinetic.moving| Boolean | OnChange/equalTo | Value (true/false) | | vehicle.kinetic.speed | Number | equalTo/greaterThan/ lowerThan/ | Value | | vehicle.trip| Literal | OnChange| Value(IDTRIP) | | vehicle.maintenance.daysBeforeMaintenance, | Number | OnChange/equalTo/ greaterThan/ lowerThan/ | Value | | vehicle.maintenance.mileageBeforeMaintenance| Number | OnChange/equalTo/ greaterThan/ lowerThan/ | Value | | vehicle.safety.beltWarning | Enum(beltWarning) | OnChange/equalTo | Value | | environment.air.temp | Number | equalTo/greaterThan/lowerThan/ | Value | | privacy.state | Enum(Privacy) | equalTo / OnChange/IncludedIN | Value |   # noqa: E501

        :param data: The data of this DataTrigger.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501
        allowed_values = ["vehicle.alert", "vehicle.odometer", "vehicle.engines.running", "vehicle.engines.thermic.oil.temp", "vehicle.energy.electric.level", "vehicle.energy.electric.autonomy", "vehicle.energy.fuel.level", "vehicle.energy.fuel.autonomy", "vehicle.autonomy", "vehicle.energy.charging.status", "vehicle.energy.charging.plugged", "vehicle.doorsState.lockedState", "vehicle.doorsState.opening", "vehicle.kinetic.moving", "vehicle.kinetic.speed", "vehicle.trip", "vehicle.maintenance.daysBeforeMaintenance", "vehicle.maintenance.mileageBeforeMaintenance", "vehicle.safety.beltWarning", "environment.air.temp", "privacy.state"]  # noqa: E501
        if data not in allowed_values:
            raise ValueError(
                "Invalid value for `data` ({0}), must be one of {1}"  # noqa: E501
                .format(data, allowed_values)
            )

        self._data = data

    @property
    def op(self):
        """Gets the op of this DataTrigger.  # noqa: E501

        The operator of the trigger function.  # noqa: E501

        :return: The op of this DataTrigger.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this DataTrigger.

        The operator of the trigger function.  # noqa: E501

        :param op: The op of this DataTrigger.  # noqa: E501
        :type: str
        """
        if op is None:
            raise ValueError("Invalid value for `op`, must not be `None`")  # noqa: E501
        allowed_values = ["equalsTo", "greaterThan", "lowerThan", "includedIn", "onChange"]  # noqa: E501
        if op not in allowed_values:
            raise ValueError(
                "Invalid value for `op` ({0}), must be one of {1}"  # noqa: E501
                .format(op, allowed_values)
            )

        self._op = op

    @property
    def value(self):
        """Gets the value of this DataTrigger.  # noqa: E501

        The right operand of the trigger function. It can be a uniq ```value``` or a list of value ```values```. The choice of one or the other depends on ```OP```  which in the case of ```includedIn``` must be a list.   * _Disclaimer_: If the op field is not set to ```includeIn``` then only the first item will be used.   # noqa: E501

        :return: The value of this DataTrigger.  # noqa: E501
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DataTrigger.

        The right operand of the trigger function. It can be a uniq ```value``` or a list of value ```values```. The choice of one or the other depends on ```OP```  which in the case of ```includedIn``` must be a list.   * _Disclaimer_: If the op field is not set to ```includeIn``` then only the first item will be used.   # noqa: E501

        :param value: The value of this DataTrigger.  # noqa: E501
        :type: list[str]
        """

        self._value = value

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
        if issubclass(DataTrigger, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DataTrigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other