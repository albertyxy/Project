// Auto-generated. Do not edit!

// (in-package V2X_Integration.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class SARA_06_Msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.SARA_06_CRC = null;
      this.SARA_06_BZ = null;
      this.SARA_Accel_X_010 = null;
      this.SARA_Accel_Y_010 = null;
      this.SARA_Omega_Z_010 = null;
      this.SARA_CF_Accel_X_010 = null;
      this.SARA_CF_Accel_Y_010 = null;
      this.SARA_CF_Omega_Z_010 = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('SARA_06_CRC')) {
        this.SARA_06_CRC = initObj.SARA_06_CRC
      }
      else {
        this.SARA_06_CRC = 0;
      }
      if (initObj.hasOwnProperty('SARA_06_BZ')) {
        this.SARA_06_BZ = initObj.SARA_06_BZ
      }
      else {
        this.SARA_06_BZ = 0;
      }
      if (initObj.hasOwnProperty('SARA_Accel_X_010')) {
        this.SARA_Accel_X_010 = initObj.SARA_Accel_X_010
      }
      else {
        this.SARA_Accel_X_010 = 0.0;
      }
      if (initObj.hasOwnProperty('SARA_Accel_Y_010')) {
        this.SARA_Accel_Y_010 = initObj.SARA_Accel_Y_010
      }
      else {
        this.SARA_Accel_Y_010 = 0.0;
      }
      if (initObj.hasOwnProperty('SARA_Omega_Z_010')) {
        this.SARA_Omega_Z_010 = initObj.SARA_Omega_Z_010
      }
      else {
        this.SARA_Omega_Z_010 = 0.0;
      }
      if (initObj.hasOwnProperty('SARA_CF_Accel_X_010')) {
        this.SARA_CF_Accel_X_010 = initObj.SARA_CF_Accel_X_010
      }
      else {
        this.SARA_CF_Accel_X_010 = 0;
      }
      if (initObj.hasOwnProperty('SARA_CF_Accel_Y_010')) {
        this.SARA_CF_Accel_Y_010 = initObj.SARA_CF_Accel_Y_010
      }
      else {
        this.SARA_CF_Accel_Y_010 = 0;
      }
      if (initObj.hasOwnProperty('SARA_CF_Omega_Z_010')) {
        this.SARA_CF_Omega_Z_010 = initObj.SARA_CF_Omega_Z_010
      }
      else {
        this.SARA_CF_Omega_Z_010 = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SARA_06_Msg
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [SARA_06_CRC]
    bufferOffset = _serializer.uint16(obj.SARA_06_CRC, buffer, bufferOffset);
    // Serialize message field [SARA_06_BZ]
    bufferOffset = _serializer.uint8(obj.SARA_06_BZ, buffer, bufferOffset);
    // Serialize message field [SARA_Accel_X_010]
    bufferOffset = _serializer.float32(obj.SARA_Accel_X_010, buffer, bufferOffset);
    // Serialize message field [SARA_Accel_Y_010]
    bufferOffset = _serializer.float32(obj.SARA_Accel_Y_010, buffer, bufferOffset);
    // Serialize message field [SARA_Omega_Z_010]
    bufferOffset = _serializer.float32(obj.SARA_Omega_Z_010, buffer, bufferOffset);
    // Serialize message field [SARA_CF_Accel_X_010]
    bufferOffset = _serializer.uint8(obj.SARA_CF_Accel_X_010, buffer, bufferOffset);
    // Serialize message field [SARA_CF_Accel_Y_010]
    bufferOffset = _serializer.uint8(obj.SARA_CF_Accel_Y_010, buffer, bufferOffset);
    // Serialize message field [SARA_CF_Omega_Z_010]
    bufferOffset = _serializer.uint8(obj.SARA_CF_Omega_Z_010, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SARA_06_Msg
    let len;
    let data = new SARA_06_Msg(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [SARA_06_CRC]
    data.SARA_06_CRC = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [SARA_06_BZ]
    data.SARA_06_BZ = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [SARA_Accel_X_010]
    data.SARA_Accel_X_010 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [SARA_Accel_Y_010]
    data.SARA_Accel_Y_010 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [SARA_Omega_Z_010]
    data.SARA_Omega_Z_010 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [SARA_CF_Accel_X_010]
    data.SARA_CF_Accel_X_010 = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [SARA_CF_Accel_Y_010]
    data.SARA_CF_Accel_Y_010 = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [SARA_CF_Omega_Z_010]
    data.SARA_CF_Omega_Z_010 = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 18;
  }

  static datatype() {
    // Returns string type for a message object
    return 'V2X_Integration/SARA_06_Msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2d6f91f1b10aaef29935d4bdfc80abae';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    uint16 SARA_06_CRC
    uint8 SARA_06_BZ
    float32 SARA_Accel_X_010
    float32 SARA_Accel_Y_010
    float32 SARA_Omega_Z_010
    uint8 SARA_CF_Accel_X_010
    uint8 SARA_CF_Accel_Y_010
    uint8 SARA_CF_Omega_Z_010
    
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SARA_06_Msg(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.SARA_06_CRC !== undefined) {
      resolved.SARA_06_CRC = msg.SARA_06_CRC;
    }
    else {
      resolved.SARA_06_CRC = 0
    }

    if (msg.SARA_06_BZ !== undefined) {
      resolved.SARA_06_BZ = msg.SARA_06_BZ;
    }
    else {
      resolved.SARA_06_BZ = 0
    }

    if (msg.SARA_Accel_X_010 !== undefined) {
      resolved.SARA_Accel_X_010 = msg.SARA_Accel_X_010;
    }
    else {
      resolved.SARA_Accel_X_010 = 0.0
    }

    if (msg.SARA_Accel_Y_010 !== undefined) {
      resolved.SARA_Accel_Y_010 = msg.SARA_Accel_Y_010;
    }
    else {
      resolved.SARA_Accel_Y_010 = 0.0
    }

    if (msg.SARA_Omega_Z_010 !== undefined) {
      resolved.SARA_Omega_Z_010 = msg.SARA_Omega_Z_010;
    }
    else {
      resolved.SARA_Omega_Z_010 = 0.0
    }

    if (msg.SARA_CF_Accel_X_010 !== undefined) {
      resolved.SARA_CF_Accel_X_010 = msg.SARA_CF_Accel_X_010;
    }
    else {
      resolved.SARA_CF_Accel_X_010 = 0
    }

    if (msg.SARA_CF_Accel_Y_010 !== undefined) {
      resolved.SARA_CF_Accel_Y_010 = msg.SARA_CF_Accel_Y_010;
    }
    else {
      resolved.SARA_CF_Accel_Y_010 = 0
    }

    if (msg.SARA_CF_Omega_Z_010 !== undefined) {
      resolved.SARA_CF_Omega_Z_010 = msg.SARA_CF_Omega_Z_010;
    }
    else {
      resolved.SARA_CF_Omega_Z_010 = 0
    }

    return resolved;
    }
};

module.exports = SARA_06_Msg;
