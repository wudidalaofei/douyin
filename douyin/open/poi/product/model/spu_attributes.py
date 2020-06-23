# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

import pprint
import re  # noqa: F401

import six


class SpuAttributes(object):
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
        '_1201': 'list[SpuAttributes1201]',
        '_1202': 'str',
        '_1203': 'int',
        '_1204': 'float',
        '_1205': 'str',
        '_1206': 'list[str]',
        '_1207': 'str',
        '_1208': 'str',
        '_1209': 'SpuAttributes1209',
        '_1210': 'str',
        '_1211': 'SpuAttributes1211',
        '_1212': 'SpuAttributes1212',
        '_1213': 'SpuAttributes1213',
        '_1214': 'int',
        '_90201': 'SpuAttributes90201',
        '_90202': 'int',
        '_90203': 'int',
        '_90204': 'int',
        '_90205': 'SpuAttributes90205'
    }

    attribute_map = {
        '_1201': '1201',
        '_1202': '1202',
        '_1203': '1203',
        '_1204': '1204',
        '_1205': '1205',
        '_1206': '1206',
        '_1207': '1207',
        '_1208': '1208',
        '_1209': '1209',
        '_1210': '1210',
        '_1211': '1211',
        '_1212': '1212',
        '_1213': '1213',
        '_1214': '1214',
        '_90201': '90201',
        '_90202': '90202',
        '_90203': '90203',
        '_90204': '90204',
        '_90205': '90205'
    }

    def __init__(self, _1201=None, _1202=None, _1203=None, _1204=None, _1205=None, _1206=None, _1207=None, _1208=None, _1209=None, _1210=None, _1211=None, _1212=None, _1213=None, _1214=None, _90201=None, _90202=None, _90203=None, _90204=None, _90205=None):  # noqa: E501
        """SpuAttributes - a model defined in Swagger"""  # noqa: E501
        self.__1201 = None
        self.__1202 = None
        self.__1203 = None
        self.__1204 = None
        self.__1205 = None
        self.__1206 = None
        self.__1207 = None
        self.__1208 = None
        self.__1209 = None
        self.__1210 = None
        self.__1211 = None
        self.__1212 = None
        self.__1213 = None
        self.__1214 = None
        self.__90201 = None
        self.__90202 = None
        self.__90203 = None
        self.__90204 = None
        self.__90205 = None
        self.discriminator = None
        if _1201 is not None:
            self._1201 = _1201
        if _1202 is not None:
            self._1202 = _1202
        if _1203 is not None:
            self._1203 = _1203
        if _1204 is not None:
            self._1204 = _1204
        if _1205 is not None:
            self._1205 = _1205
        if _1206 is not None:
            self._1206 = _1206
        if _1207 is not None:
            self._1207 = _1207
        if _1208 is not None:
            self._1208 = _1208
        if _1209 is not None:
            self._1209 = _1209
        if _1210 is not None:
            self._1210 = _1210
        if _1211 is not None:
            self._1211 = _1211
        if _1212 is not None:
            self._1212 = _1212
        if _1213 is not None:
            self._1213 = _1213
        if _1214 is not None:
            self._1214 = _1214
        if _90201 is not None:
            self._90201 = _90201
        if _90202 is not None:
            self._90202 = _90202
        if _90203 is not None:
            self._90203 = _90203
        if _90204 is not None:
            self._90204 = _90204
        if _90205 is not None:
            self._90205 = _90205

    @property
    def _1201(self):
        """Gets the _1201 of this SpuAttributes.  # noqa: E501

        设施列表  # noqa: E501

        :return: The _1201 of this SpuAttributes.  # noqa: E501
        :rtype: list[SpuAttributes1201]
        """
        return self.__1201

    @_1201.setter
    def _1201(self, _1201):
        """Sets the _1201 of this SpuAttributes.

        设施列表  # noqa: E501

        :param _1201: The _1201 of this SpuAttributes.  # noqa: E501
        :type: list[SpuAttributes1201]
        """

        self.__1201 = _1201

    @property
    def _1202(self):
        """Gets the _1202 of this SpuAttributes.  # noqa: E501

        床型名称  # noqa: E501

        :return: The _1202 of this SpuAttributes.  # noqa: E501
        :rtype: str
        """
        return self.__1202

    @_1202.setter
    def _1202(self, _1202):
        """Sets the _1202 of this SpuAttributes.

        床型名称  # noqa: E501

        :param _1202: The _1202 of this SpuAttributes.  # noqa: E501
        :type: str
        """

        self.__1202 = _1202

    @property
    def _1203(self):
        """Gets the _1203 of this SpuAttributes.  # noqa: E501

        可住人数  # noqa: E501

        :return: The _1203 of this SpuAttributes.  # noqa: E501
        :rtype: int
        """
        return self.__1203

    @_1203.setter
    def _1203(self, _1203):
        """Sets the _1203 of this SpuAttributes.

        可住人数  # noqa: E501

        :param _1203: The _1203 of this SpuAttributes.  # noqa: E501
        :type: int
        """

        self.__1203 = _1203

    @property
    def _1204(self):
        """Gets the _1204 of this SpuAttributes.  # noqa: E501

        面积(平方米)  # noqa: E501

        :return: The _1204 of this SpuAttributes.  # noqa: E501
        :rtype: float
        """
        return self.__1204

    @_1204.setter
    def _1204(self, _1204):
        """Sets the _1204 of this SpuAttributes.

        面积(平方米)  # noqa: E501

        :param _1204: The _1204 of this SpuAttributes.  # noqa: E501
        :type: float
        """

        self.__1204 = _1204

    @property
    def _1205(self):
        """Gets the _1205 of this SpuAttributes.  # noqa: E501

        房型封面图  # noqa: E501

        :return: The _1205 of this SpuAttributes.  # noqa: E501
        :rtype: str
        """
        return self.__1205

    @_1205.setter
    def _1205(self, _1205):
        """Sets the _1205 of this SpuAttributes.

        房型封面图  # noqa: E501

        :param _1205: The _1205 of this SpuAttributes.  # noqa: E501
        :type: str
        """

        self.__1205 = _1205

    @property
    def _1206(self):
        """Gets the _1206 of this SpuAttributes.  # noqa: E501

        房型相册  # noqa: E501

        :return: The _1206 of this SpuAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self.__1206

    @_1206.setter
    def _1206(self, _1206):
        """Sets the _1206 of this SpuAttributes.

        房型相册  # noqa: E501

        :param _1206: The _1206 of this SpuAttributes.  # noqa: E501
        :type: list[str]
        """

        self.__1206 = _1206

    @property
    def _1207(self):
        """Gets the _1207 of this SpuAttributes.  # noqa: E501

        房型简介  # noqa: E501

        :return: The _1207 of this SpuAttributes.  # noqa: E501
        :rtype: str
        """
        return self.__1207

    @_1207.setter
    def _1207(self, _1207):
        """Sets the _1207 of this SpuAttributes.

        房型简介  # noqa: E501

        :param _1207: The _1207 of this SpuAttributes.  # noqa: E501
        :type: str
        """

        self.__1207 = _1207

    @property
    def _1208(self):
        """Gets the _1208 of this SpuAttributes.  # noqa: E501

        相关政策  # noqa: E501

        :return: The _1208 of this SpuAttributes.  # noqa: E501
        :rtype: str
        """
        return self.__1208

    @_1208.setter
    def _1208(self, _1208):
        """Sets the _1208 of this SpuAttributes.

        相关政策  # noqa: E501

        :param _1208: The _1208 of this SpuAttributes.  # noqa: E501
        :type: str
        """

        self.__1208 = _1208

    @property
    def _1209(self):
        """Gets the _1209 of this SpuAttributes.  # noqa: E501


        :return: The _1209 of this SpuAttributes.  # noqa: E501
        :rtype: SpuAttributes1209
        """
        return self.__1209

    @_1209.setter
    def _1209(self, _1209):
        """Sets the _1209 of this SpuAttributes.


        :param _1209: The _1209 of this SpuAttributes.  # noqa: E501
        :type: SpuAttributes1209
        """

        self.__1209 = _1209

    @property
    def _1210(self):
        """Gets the _1210 of this SpuAttributes.  # noqa: E501

        景观  # noqa: E501

        :return: The _1210 of this SpuAttributes.  # noqa: E501
        :rtype: str
        """
        return self.__1210

    @_1210.setter
    def _1210(self, _1210):
        """Sets the _1210 of this SpuAttributes.

        景观  # noqa: E501

        :param _1210: The _1210 of this SpuAttributes.  # noqa: E501
        :type: str
        """

        self.__1210 = _1210

    @property
    def _1211(self):
        """Gets the _1211 of this SpuAttributes.  # noqa: E501


        :return: The _1211 of this SpuAttributes.  # noqa: E501
        :rtype: SpuAttributes1211
        """
        return self.__1211

    @_1211.setter
    def _1211(self, _1211):
        """Sets the _1211 of this SpuAttributes.


        :param _1211: The _1211 of this SpuAttributes.  # noqa: E501
        :type: SpuAttributes1211
        """

        self.__1211 = _1211

    @property
    def _1212(self):
        """Gets the _1212 of this SpuAttributes.  # noqa: E501


        :return: The _1212 of this SpuAttributes.  # noqa: E501
        :rtype: SpuAttributes1212
        """
        return self.__1212

    @_1212.setter
    def _1212(self, _1212):
        """Sets the _1212 of this SpuAttributes.


        :param _1212: The _1212 of this SpuAttributes.  # noqa: E501
        :type: SpuAttributes1212
        """

        self.__1212 = _1212

    @property
    def _1213(self):
        """Gets the _1213 of this SpuAttributes.  # noqa: E501


        :return: The _1213 of this SpuAttributes.  # noqa: E501
        :rtype: SpuAttributes1213
        """
        return self.__1213

    @_1213.setter
    def _1213(self, _1213):
        """Sets the _1213 of this SpuAttributes.


        :param _1213: The _1213 of this SpuAttributes.  # noqa: E501
        :type: SpuAttributes1213
        """

        self.__1213 = _1213

    @property
    def _1214(self):
        """Gets the _1214 of this SpuAttributes.  # noqa: E501

        早餐; 0 - 无早餐; 1~9 - n份早餐; 10 - 多份早餐  # noqa: E501

        :return: The _1214 of this SpuAttributes.  # noqa: E501
        :rtype: int
        """
        return self.__1214

    @_1214.setter
    def _1214(self, _1214):
        """Sets the _1214 of this SpuAttributes.

        早餐; 0 - 无早餐; 1~9 - n份早餐; 10 - 多份早餐  # noqa: E501

        :param _1214: The _1214 of this SpuAttributes.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # noqa: E501
        if _1214 not in allowed_values:
            raise ValueError(
                "Invalid value for `_1214` ({0}), must be one of {1}"  # noqa: E501
                .format(_1214, allowed_values)
            )

        self.__1214 = _1214

    @property
    def _90201(self):
        """Gets the _90201 of this SpuAttributes.  # noqa: E501


        :return: The _90201 of this SpuAttributes.  # noqa: E501
        :rtype: SpuAttributes90201
        """
        return self.__90201

    @_90201.setter
    def _90201(self, _90201):
        """Sets the _90201 of this SpuAttributes.


        :param _90201: The _90201 of this SpuAttributes.  # noqa: E501
        :type: SpuAttributes90201
        """

        self.__90201 = _90201

    @property
    def _90202(self):
        """Gets the _90202 of this SpuAttributes.  # noqa: E501

        是否可退 1- 随时退，2-不可退, 3-有条件退  # noqa: E501

        :return: The _90202 of this SpuAttributes.  # noqa: E501
        :rtype: int
        """
        return self.__90202

    @_90202.setter
    def _90202(self, _90202):
        """Sets the _90202 of this SpuAttributes.

        是否可退 1- 随时退，2-不可退, 3-有条件退  # noqa: E501

        :param _90202: The _90202 of this SpuAttributes.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3]  # noqa: E501
        if _90202 not in allowed_values:
            raise ValueError(
                "Invalid value for `_90202` ({0}), must be one of {1}"  # noqa: E501
                .format(_90202, allowed_values)
            )

        self.__90202 = _90202

    @property
    def _90203(self):
        """Gets the _90203 of this SpuAttributes.  # noqa: E501

        取票信息 1-需要取票 2-无需取票  # noqa: E501

        :return: The _90203 of this SpuAttributes.  # noqa: E501
        :rtype: int
        """
        return self.__90203

    @_90203.setter
    def _90203(self, _90203):
        """Sets the _90203 of this SpuAttributes.

        取票信息 1-需要取票 2-无需取票  # noqa: E501

        :param _90203: The _90203 of this SpuAttributes.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2]  # noqa: E501
        if _90203 not in allowed_values:
            raise ValueError(
                "Invalid value for `_90203` ({0}), must be one of {1}"  # noqa: E501
                .format(_90203, allowed_values)
            )

        self.__90203 = _90203

    @property
    def _90204(self):
        """Gets the _90204 of this SpuAttributes.  # noqa: E501

        门票价格(展示最近7日最低价，精确到分)  # noqa: E501

        :return: The _90204 of this SpuAttributes.  # noqa: E501
        :rtype: int
        """
        return self.__90204

    @_90204.setter
    def _90204(self, _90204):
        """Sets the _90204 of this SpuAttributes.

        门票价格(展示最近7日最低价，精确到分)  # noqa: E501

        :param _90204: The _90204 of this SpuAttributes.  # noqa: E501
        :type: int
        """

        self.__90204 = _90204

    @property
    def _90205(self):
        """Gets the _90205 of this SpuAttributes.  # noqa: E501


        :return: The _90205 of this SpuAttributes.  # noqa: E501
        :rtype: SpuAttributes90205
        """
        return self.__90205

    @_90205.setter
    def _90205(self, _90205):
        """Sets the _90205 of this SpuAttributes.


        :param _90205: The _90205 of this SpuAttributes.  # noqa: E501
        :type: SpuAttributes90205
        """

        self.__90205 = _90205

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
        if issubclass(SpuAttributes, dict):
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
        if not isinstance(other, SpuAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other