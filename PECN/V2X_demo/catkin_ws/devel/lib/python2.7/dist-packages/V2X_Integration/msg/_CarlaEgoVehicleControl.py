# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from V2X_Integration/CarlaEgoVehicleControl.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class CarlaEgoVehicleControl(genpy.Message):
  _md5sum = "e5b57fc698c12ff4c20a5fc71fba832f"
  _type = "V2X_Integration/CarlaEgoVehicleControl"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """#
# Copyright (c) 2018-2019 Intel Corporation.
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.
#
# This represents a vehicle control message sent to CARLA simulator

std_msgs/Header header

# The CARLA vehicle control data

# 0. <= throttle <= 1.
float32 throttle

# -1. <= steer <= 1.
float32 steer

# 0. <= brake <= 1.
float32 brake

# hand_brake 0 or 1
bool hand_brake

# reverse 0 or 1
bool reverse

# gear
int32 gear

# manual gear shift
bool manual_gear_shift

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  __slots__ = ['header','throttle','steer','brake','hand_brake','reverse','gear','manual_gear_shift']
  _slot_types = ['std_msgs/Header','float32','float32','float32','bool','bool','int32','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,throttle,steer,brake,hand_brake,reverse,gear,manual_gear_shift

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CarlaEgoVehicleControl, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.throttle is None:
        self.throttle = 0.
      if self.steer is None:
        self.steer = 0.
      if self.brake is None:
        self.brake = 0.
      if self.hand_brake is None:
        self.hand_brake = False
      if self.reverse is None:
        self.reverse = False
      if self.gear is None:
        self.gear = 0
      if self.manual_gear_shift is None:
        self.manual_gear_shift = False
    else:
      self.header = std_msgs.msg.Header()
      self.throttle = 0.
      self.steer = 0.
      self.brake = 0.
      self.hand_brake = False
      self.reverse = False
      self.gear = 0
      self.manual_gear_shift = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3f2BiB().pack(_x.throttle, _x.steer, _x.brake, _x.hand_brake, _x.reverse, _x.gear, _x.manual_gear_shift))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 19
      (_x.throttle, _x.steer, _x.brake, _x.hand_brake, _x.reverse, _x.gear, _x.manual_gear_shift,) = _get_struct_3f2BiB().unpack(str[start:end])
      self.hand_brake = bool(self.hand_brake)
      self.reverse = bool(self.reverse)
      self.manual_gear_shift = bool(self.manual_gear_shift)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3f2BiB().pack(_x.throttle, _x.steer, _x.brake, _x.hand_brake, _x.reverse, _x.gear, _x.manual_gear_shift))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 19
      (_x.throttle, _x.steer, _x.brake, _x.hand_brake, _x.reverse, _x.gear, _x.manual_gear_shift,) = _get_struct_3f2BiB().unpack(str[start:end])
      self.hand_brake = bool(self.hand_brake)
      self.reverse = bool(self.reverse)
      self.manual_gear_shift = bool(self.manual_gear_shift)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3f2BiB = None
def _get_struct_3f2BiB():
    global _struct_3f2BiB
    if _struct_3f2BiB is None:
        _struct_3f2BiB = struct.Struct("<3f2BiB")
    return _struct_3f2BiB
