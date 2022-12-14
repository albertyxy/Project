# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from V2X_Integration/ESP_21_Msg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class ESP_21_Msg(genpy.Message):
  _md5sum = "14034e15be32d792bb36bad51c5aaa1b"
  _type = "V2X_Integration/ESP_21_Msg"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
uint16 ESP_21_CRC
uint8 ESP_21_BZ
int16 BR_Eingriffsmoment
uint8 ESP_Diagnose
uint8 ESC_v_Signal_Qualifier_High_Low
uint8 ESP_Vorsteuerung
uint8 OBD_Schlechtweg
uint8 OBD_QBit_Schlechtweg
float32 ESP_v_Signal
uint8 ASR_Tastung_passiv
uint8 ESP_Tastung_passiv
uint8 ESP_Systemstatus
uint8 ASR_Schalteingriff
uint8 ESP_QBit_v_Signal
uint8 ABS_Bremsung
uint8 ASR_Anf
uint8 MSR_Anf
uint8 EBV_Eingriff
uint8 EDS_Eingriff
uint8 ESP_Eingriff
uint8 ESP_ASP
uint8 ESC_Neutralschaltung

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
  __slots__ = ['header','ESP_21_CRC','ESP_21_BZ','BR_Eingriffsmoment','ESP_Diagnose','ESC_v_Signal_Qualifier_High_Low','ESP_Vorsteuerung','OBD_Schlechtweg','OBD_QBit_Schlechtweg','ESP_v_Signal','ASR_Tastung_passiv','ESP_Tastung_passiv','ESP_Systemstatus','ASR_Schalteingriff','ESP_QBit_v_Signal','ABS_Bremsung','ASR_Anf','MSR_Anf','EBV_Eingriff','EDS_Eingriff','ESP_Eingriff','ESP_ASP','ESC_Neutralschaltung']
  _slot_types = ['std_msgs/Header','uint16','uint8','int16','uint8','uint8','uint8','uint8','uint8','float32','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,ESP_21_CRC,ESP_21_BZ,BR_Eingriffsmoment,ESP_Diagnose,ESC_v_Signal_Qualifier_High_Low,ESP_Vorsteuerung,OBD_Schlechtweg,OBD_QBit_Schlechtweg,ESP_v_Signal,ASR_Tastung_passiv,ESP_Tastung_passiv,ESP_Systemstatus,ASR_Schalteingriff,ESP_QBit_v_Signal,ABS_Bremsung,ASR_Anf,MSR_Anf,EBV_Eingriff,EDS_Eingriff,ESP_Eingriff,ESP_ASP,ESC_Neutralschaltung

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ESP_21_Msg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.ESP_21_CRC is None:
        self.ESP_21_CRC = 0
      if self.ESP_21_BZ is None:
        self.ESP_21_BZ = 0
      if self.BR_Eingriffsmoment is None:
        self.BR_Eingriffsmoment = 0
      if self.ESP_Diagnose is None:
        self.ESP_Diagnose = 0
      if self.ESC_v_Signal_Qualifier_High_Low is None:
        self.ESC_v_Signal_Qualifier_High_Low = 0
      if self.ESP_Vorsteuerung is None:
        self.ESP_Vorsteuerung = 0
      if self.OBD_Schlechtweg is None:
        self.OBD_Schlechtweg = 0
      if self.OBD_QBit_Schlechtweg is None:
        self.OBD_QBit_Schlechtweg = 0
      if self.ESP_v_Signal is None:
        self.ESP_v_Signal = 0.
      if self.ASR_Tastung_passiv is None:
        self.ASR_Tastung_passiv = 0
      if self.ESP_Tastung_passiv is None:
        self.ESP_Tastung_passiv = 0
      if self.ESP_Systemstatus is None:
        self.ESP_Systemstatus = 0
      if self.ASR_Schalteingriff is None:
        self.ASR_Schalteingriff = 0
      if self.ESP_QBit_v_Signal is None:
        self.ESP_QBit_v_Signal = 0
      if self.ABS_Bremsung is None:
        self.ABS_Bremsung = 0
      if self.ASR_Anf is None:
        self.ASR_Anf = 0
      if self.MSR_Anf is None:
        self.MSR_Anf = 0
      if self.EBV_Eingriff is None:
        self.EBV_Eingriff = 0
      if self.EDS_Eingriff is None:
        self.EDS_Eingriff = 0
      if self.ESP_Eingriff is None:
        self.ESP_Eingriff = 0
      if self.ESP_ASP is None:
        self.ESP_ASP = 0
      if self.ESC_Neutralschaltung is None:
        self.ESC_Neutralschaltung = 0
    else:
      self.header = std_msgs.msg.Header()
      self.ESP_21_CRC = 0
      self.ESP_21_BZ = 0
      self.BR_Eingriffsmoment = 0
      self.ESP_Diagnose = 0
      self.ESC_v_Signal_Qualifier_High_Low = 0
      self.ESP_Vorsteuerung = 0
      self.OBD_Schlechtweg = 0
      self.OBD_QBit_Schlechtweg = 0
      self.ESP_v_Signal = 0.
      self.ASR_Tastung_passiv = 0
      self.ESP_Tastung_passiv = 0
      self.ESP_Systemstatus = 0
      self.ASR_Schalteingriff = 0
      self.ESP_QBit_v_Signal = 0
      self.ABS_Bremsung = 0
      self.ASR_Anf = 0
      self.MSR_Anf = 0
      self.EBV_Eingriff = 0
      self.EDS_Eingriff = 0
      self.ESP_Eingriff = 0
      self.ESP_ASP = 0
      self.ESC_Neutralschaltung = 0

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
      buff.write(_get_struct_HBh5Bf13B().pack(_x.ESP_21_CRC, _x.ESP_21_BZ, _x.BR_Eingriffsmoment, _x.ESP_Diagnose, _x.ESC_v_Signal_Qualifier_High_Low, _x.ESP_Vorsteuerung, _x.OBD_Schlechtweg, _x.OBD_QBit_Schlechtweg, _x.ESP_v_Signal, _x.ASR_Tastung_passiv, _x.ESP_Tastung_passiv, _x.ESP_Systemstatus, _x.ASR_Schalteingriff, _x.ESP_QBit_v_Signal, _x.ABS_Bremsung, _x.ASR_Anf, _x.MSR_Anf, _x.EBV_Eingriff, _x.EDS_Eingriff, _x.ESP_Eingriff, _x.ESP_ASP, _x.ESC_Neutralschaltung))
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
      end += 27
      (_x.ESP_21_CRC, _x.ESP_21_BZ, _x.BR_Eingriffsmoment, _x.ESP_Diagnose, _x.ESC_v_Signal_Qualifier_High_Low, _x.ESP_Vorsteuerung, _x.OBD_Schlechtweg, _x.OBD_QBit_Schlechtweg, _x.ESP_v_Signal, _x.ASR_Tastung_passiv, _x.ESP_Tastung_passiv, _x.ESP_Systemstatus, _x.ASR_Schalteingriff, _x.ESP_QBit_v_Signal, _x.ABS_Bremsung, _x.ASR_Anf, _x.MSR_Anf, _x.EBV_Eingriff, _x.EDS_Eingriff, _x.ESP_Eingriff, _x.ESP_ASP, _x.ESC_Neutralschaltung,) = _get_struct_HBh5Bf13B().unpack(str[start:end])
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
      buff.write(_get_struct_HBh5Bf13B().pack(_x.ESP_21_CRC, _x.ESP_21_BZ, _x.BR_Eingriffsmoment, _x.ESP_Diagnose, _x.ESC_v_Signal_Qualifier_High_Low, _x.ESP_Vorsteuerung, _x.OBD_Schlechtweg, _x.OBD_QBit_Schlechtweg, _x.ESP_v_Signal, _x.ASR_Tastung_passiv, _x.ESP_Tastung_passiv, _x.ESP_Systemstatus, _x.ASR_Schalteingriff, _x.ESP_QBit_v_Signal, _x.ABS_Bremsung, _x.ASR_Anf, _x.MSR_Anf, _x.EBV_Eingriff, _x.EDS_Eingriff, _x.ESP_Eingriff, _x.ESP_ASP, _x.ESC_Neutralschaltung))
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
      end += 27
      (_x.ESP_21_CRC, _x.ESP_21_BZ, _x.BR_Eingriffsmoment, _x.ESP_Diagnose, _x.ESC_v_Signal_Qualifier_High_Low, _x.ESP_Vorsteuerung, _x.OBD_Schlechtweg, _x.OBD_QBit_Schlechtweg, _x.ESP_v_Signal, _x.ASR_Tastung_passiv, _x.ESP_Tastung_passiv, _x.ESP_Systemstatus, _x.ASR_Schalteingriff, _x.ESP_QBit_v_Signal, _x.ABS_Bremsung, _x.ASR_Anf, _x.MSR_Anf, _x.EBV_Eingriff, _x.EDS_Eingriff, _x.ESP_Eingriff, _x.ESP_ASP, _x.ESC_Neutralschaltung,) = _get_struct_HBh5Bf13B().unpack(str[start:end])
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
_struct_HBh5Bf13B = None
def _get_struct_HBh5Bf13B():
    global _struct_HBh5Bf13B
    if _struct_HBh5Bf13B is None:
        _struct_HBh5Bf13B = struct.Struct("<HBh5Bf13B")
    return _struct_HBh5Bf13B
