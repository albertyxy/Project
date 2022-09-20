// Auto-generated. Do not edit!

// (in-package V2X_Integration.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class V2X_Warning {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.warning_level = null;
    }
    else {
      if (initObj.hasOwnProperty('warning_level')) {
        this.warning_level = initObj.warning_level
      }
      else {
        this.warning_level = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type V2X_Warning
    // Serialize message field [warning_level]
    bufferOffset = _serializer.uint8(obj.warning_level, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type V2X_Warning
    let len;
    let data = new V2X_Warning(null);
    // Deserialize message field [warning_level]
    data.warning_level = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a message object
    return 'V2X_Integration/V2X_Warning';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '140cc051af28c9742e4f2dcebd133a9b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 warning_level
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new V2X_Warning(null);
    if (msg.warning_level !== undefined) {
      resolved.warning_level = msg.warning_level;
    }
    else {
      resolved.warning_level = 0
    }

    return resolved;
    }
};

module.exports = V2X_Warning;
