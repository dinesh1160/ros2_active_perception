# generated from rosidl_generator_py/resource/_idl.py.em
# with input from active_perception_interfaces:srv/AnalyzeQuality.idl
# generated code does not contain a copyright notice

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
from os import getenv

ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AnalyzeQuality_Request(type):
    """Metaclass of message 'AnalyzeQuality_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('active_perception_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'active_perception_interfaces.srv.AnalyzeQuality_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__analyze_quality__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__analyze_quality__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__analyze_quality__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__analyze_quality__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__analyze_quality__request

            from sensor_msgs.msg import Image
            if Image.__class__._TYPE_SUPPORT is None:
                Image.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AnalyzeQuality_Request(metaclass=Metaclass_AnalyzeQuality_Request):
    """Message class 'AnalyzeQuality_Request'."""

    __slots__ = [
        '_image',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'image': 'sensor_msgs/Image',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['sensor_msgs', 'msg'], 'Image'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from sensor_msgs.msg import Image
        self.image = kwargs.get('image', Image())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.image != other.image:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def image(self):
        """Message field 'image'."""
        return self._image

    @image.setter
    def image(self, value):
        if self._check_fields:
            from sensor_msgs.msg import Image
            assert \
                isinstance(value, Image), \
                "The 'image' field must be a sub message of type 'Image'"
        self._image = value


# Import statements for member types

# already imported above
# import builtins

import math  # noqa: E402, I100

# already imported above
# import rosidl_parser.definition


class Metaclass_AnalyzeQuality_Response(type):
    """Metaclass of message 'AnalyzeQuality_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('active_perception_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'active_perception_interfaces.srv.AnalyzeQuality_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__analyze_quality__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__analyze_quality__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__analyze_quality__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__analyze_quality__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__analyze_quality__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AnalyzeQuality_Response(metaclass=Metaclass_AnalyzeQuality_Response):
    """Message class 'AnalyzeQuality_Response'."""

    __slots__ = [
        '_occlusion_score',
        '_framing_score',
        '_reasoning',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'occlusion_score': 'float',
        'framing_score': 'float',
        'reasoning': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.occlusion_score = kwargs.get('occlusion_score', float())
        self.framing_score = kwargs.get('framing_score', float())
        self.reasoning = kwargs.get('reasoning', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.occlusion_score != other.occlusion_score:
            return False
        if self.framing_score != other.framing_score:
            return False
        if self.reasoning != other.reasoning:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def occlusion_score(self):
        """Message field 'occlusion_score'."""
        return self._occlusion_score

    @occlusion_score.setter
    def occlusion_score(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'occlusion_score' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'occlusion_score' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._occlusion_score = value

    @builtins.property
    def framing_score(self):
        """Message field 'framing_score'."""
        return self._framing_score

    @framing_score.setter
    def framing_score(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'framing_score' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'framing_score' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._framing_score = value

    @builtins.property
    def reasoning(self):
        """Message field 'reasoning'."""
        return self._reasoning

    @reasoning.setter
    def reasoning(self, value):
        if self._check_fields:
            assert \
                isinstance(value, str), \
                "The 'reasoning' field must be of type 'str'"
        self._reasoning = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AnalyzeQuality_Event(type):
    """Metaclass of message 'AnalyzeQuality_Event'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('active_perception_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'active_perception_interfaces.srv.AnalyzeQuality_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__analyze_quality__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__analyze_quality__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__analyze_quality__event
            cls._TYPE_SUPPORT = module.type_support_msg__srv__analyze_quality__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__analyze_quality__event

            from service_msgs.msg import ServiceEventInfo
            if ServiceEventInfo.__class__._TYPE_SUPPORT is None:
                ServiceEventInfo.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AnalyzeQuality_Event(metaclass=Metaclass_AnalyzeQuality_Event):
    """Message class 'AnalyzeQuality_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<active_perception_interfaces/AnalyzeQuality_Request, 1>',
        'response': 'sequence<active_perception_interfaces/AnalyzeQuality_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['active_perception_interfaces', 'srv'], 'AnalyzeQuality_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['active_perception_interfaces', 'srv'], 'AnalyzeQuality_Response'), 1),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from service_msgs.msg import ServiceEventInfo
        self.info = kwargs.get('info', ServiceEventInfo())
        self.request = kwargs.get('request', [])
        self.response = kwargs.get('response', [])

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.info != other.info:
            return False
        if self.request != other.request:
            return False
        if self.response != other.response:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def info(self):
        """Message field 'info'."""
        return self._info

    @info.setter
    def info(self, value):
        if self._check_fields:
            from service_msgs.msg import ServiceEventInfo
            assert \
                isinstance(value, ServiceEventInfo), \
                "The 'info' field must be a sub message of type 'ServiceEventInfo'"
        self._info = value

    @builtins.property
    def request(self):
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value):
        if self._check_fields:
            from active_perception_interfaces.srv import AnalyzeQuality_Request
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 1 and
                 all(isinstance(v, AnalyzeQuality_Request) for v in value) and
                 True), \
                "The 'request' field must be a set or sequence with length <= 1 and each value of type 'AnalyzeQuality_Request'"
        self._request = value

    @builtins.property
    def response(self):
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value):
        if self._check_fields:
            from active_perception_interfaces.srv import AnalyzeQuality_Response
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 1 and
                 all(isinstance(v, AnalyzeQuality_Response) for v in value) and
                 True), \
                "The 'response' field must be a set or sequence with length <= 1 and each value of type 'AnalyzeQuality_Response'"
        self._response = value


class Metaclass_AnalyzeQuality(type):
    """Metaclass of service 'AnalyzeQuality'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('active_perception_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'active_perception_interfaces.srv.AnalyzeQuality')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__analyze_quality

            from active_perception_interfaces.srv import _analyze_quality
            if _analyze_quality.Metaclass_AnalyzeQuality_Request._TYPE_SUPPORT is None:
                _analyze_quality.Metaclass_AnalyzeQuality_Request.__import_type_support__()
            if _analyze_quality.Metaclass_AnalyzeQuality_Response._TYPE_SUPPORT is None:
                _analyze_quality.Metaclass_AnalyzeQuality_Response.__import_type_support__()
            if _analyze_quality.Metaclass_AnalyzeQuality_Event._TYPE_SUPPORT is None:
                _analyze_quality.Metaclass_AnalyzeQuality_Event.__import_type_support__()


class AnalyzeQuality(metaclass=Metaclass_AnalyzeQuality):
    from active_perception_interfaces.srv._analyze_quality import AnalyzeQuality_Request as Request
    from active_perception_interfaces.srv._analyze_quality import AnalyzeQuality_Response as Response
    from active_perception_interfaces.srv._analyze_quality import AnalyzeQuality_Event as Event

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
