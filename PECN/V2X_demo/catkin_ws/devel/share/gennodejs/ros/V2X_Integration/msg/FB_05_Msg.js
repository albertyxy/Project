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

class FB_05_Msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.FB_Kopfrotation_Gier_Guete = null;
      this.FB_Kopfposition_Z_Guete = null;
      this.FB_Kopfposition_Y_Guete = null;
      this.FB_Kopfposition_X_Guete = null;
      this.FB_Kopfrotation_Gier = null;
      this.FB_Kopfposition_Z = null;
      this.FB_Kopfposition_Y = null;
      this.FB_Kopfposition_X = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('FB_Kopfrotation_Gier_Guete')) {
        this.FB_Kopfrotation_Gier_Guete = initObj.FB_Kopfrotation_Gier_Guete
      }
      else {
        this.FB_Kopfrotation_Gier_Guete = 0.0;
      }
      if (initObj.hasOwnProperty('FB_Kopfposition_Z_Guete')) {
        this.FB_Kopfposition_Z_Guete = initObj.FB_Kopfposition_Z_Guete
      }
      else {
        this.FB_Kopfposition_Z_Guete = 0.0;
      }
      if (initObj.hasOwnProperty('FB_Kopfposition_Y_Guete')) {
        this.FB_Kopfposition_Y_Guete = initObj.FB_Kopfposition_Y_Guete
      }
      else {
        this.FB_Kopfposition_Y_Guete = 0.0;
      }
      if (initObj.hasOwnProperty('FB_Kopfposition_X_Guete')) {
        this.FB_Kopfposition_X_Guete = initObj.FB_Kopfposition_X_Guete
      }
      else {
        this.FB_Kopfposition_X_Guete = 0.0;
      }
      if (initObj.hasOwnProperty('FB_Kopfrotation_Gier')) {
        this.FB_Kopfrotation_Gier = initObj.FB_Kopfrotation_Gier
      }
      else {
        this.FB_Kopfrotation_Gier = 0.0;
      }
      if (initObj.hasOwnProperty('FB_Kopfposition_Z')) {
        this.FB_Kopfposition_Z = initObj.FB_Kopfposition_Z
      }
      else {
        this.FB_Kopfposition_Z = 0.0;
      }
      if (initObj.hasOwnProperty('FB_Kopfposition_Y')) {
        this.FB_Kopfposition_Y = initObj.FB_Kopfposition_Y
      }
      else {
        this.FB_Kopfposition_Y = 0.0;
      }
      if (initObj.hasOwnProperty('FB_Kopfposition_X')) {
        this.FB_Kopfposition_X = initObj.FB_Kopfposition_X
      }
      else {
        this.FB_Kopfposition_X = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FB_05_Msg
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [FB_Kopfrotation_Gier_Guete]
    bufferOffset = _serializer.float32(obj.FB_Kopfrotation_Gier_Guete, buffer, bufferOffset);
    // Serialize message field [FB_Kopfposition_Z_Guete]
    bufferOffset = _serializer.float32(obj.FB_Kopfposition_Z_Guete, buffer, bufferOffset);
    // Serialize message field [FB_Kopfposition_Y_Guete]
    bufferOffset = _serializer.float32(obj.FB_Kopfposition_Y_Guete, buffer, bufferOffset);
    // Serialize message field [FB_Kopfposition_X_Guete]
    bufferOffset = _serializer.float32(obj.FB_Kopfposition_X_Guete, buffer, bufferOffset);
    // Serialize message field [FB_Kopfrotation_Gier]
    bufferOffset = _serializer.float32(obj.FB_Kopfrotation_Gier, buffer, bufferOffset);
    // Serialize message field [FB_Kopfposition_Z]
    bufferOffset = _serializer.float32(obj.FB_Kopfposition_Z, buffer, bufferOffset);
    // Serialize message field [FB_Kopfposition_Y]
    bufferOffset = _serializer.float32(obj.FB_Kopfposition_Y, buffer, bufferOffset);
    // Serialize message field [FB_Kopfposition_X]
    bufferOffset = _serializer.float32(obj.FB_Kopfposition_X, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FB_05_Msg
    let len;
    let data = new FB_05_Msg(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [FB_Kopfrotation_Gier_Guete]
    data.FB_Kopfrotation_Gier_Guete = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [FB_Kopfposition_Z_Guete]
    data.FB_Kopfposition_Z_Guete = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [FB_Kopfposition_Y_Guete]
    data.FB_Kopfposition_Y_Guete = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [FB_Kopfposition_X_Guete]
    data.FB_Kopfposition_X_Guete = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [FB_Kopfrotation_Gier]
    data.FB_Kopfrotation_Gier = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [FB_Kopfposition_Z]
    data.FB_Kopfposition_Z = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [FB_Kopfposition_Y]
    data.FB_Kopfposition_Y = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [FB_Kopfposition_X]
    data.FB_Kopfposition_X = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'V2X_Integration/FB_05_Msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e0505810bf77d4eb9eb73dfc0b88136b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    float32 FB_Kopfrotation_Gier_Guete
    float32 FB_Kopfposition_Z_Guete
    float32 FB_Kopfposition_Y_Guete
    float32 FB_Kopfposition_X_Guete
    float32 FB_Kopfrotation_Gier
    float32 FB_Kopfposition_Z
    float32 FB_Kopfposition_Y
    float32 FB_Kopfposition_X
    
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
    const resolved = new FB_05_Msg(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.FB_Kopfrotation_Gier_Guete !== undefined) {
      resolved.FB_Kopfrotation_Gier_Guete = msg.FB_Kopfrotation_Gier_Guete;
    }
    else {
      resolved.FB_Kopfrotation_Gier_Guete = 0.0
    }

    if (msg.FB_Kopfposition_Z_Guete !== undefined) {
      resolved.FB_Kopfposition_Z_Guete = msg.FB_Kopfposition_Z_Guete;
    }
    else {
      resolved.FB_Kopfposition_Z_Guete = 0.0
    }

    if (msg.FB_Kopfposition_Y_Guete !== undefined) {
      resolved.FB_Kopfposition_Y_Guete = msg.FB_Kopfposition_Y_Guete;
    }
    else {
      resolved.FB_Kopfposition_Y_Guete = 0.0
    }

    if (msg.FB_Kopfposition_X_Guete !== undefined) {
      resolved.FB_Kopfposition_X_Guete = msg.FB_Kopfposition_X_Guete;
    }
    else {
      resolved.FB_Kopfposition_X_Guete = 0.0
    }

    if (msg.FB_Kopfrotation_Gier !== undefined) {
      resolved.FB_Kopfrotation_Gier = msg.FB_Kopfrotation_Gier;
    }
    else {
      resolved.FB_Kopfrotation_Gier = 0.0
    }

    if (msg.FB_Kopfposition_Z !== undefined) {
      resolved.FB_Kopfposition_Z = msg.FB_Kopfposition_Z;
    }
    else {
      resolved.FB_Kopfposition_Z = 0.0
    }

    if (msg.FB_Kopfposition_Y !== undefined) {
      resolved.FB_Kopfposition_Y = msg.FB_Kopfposition_Y;
    }
    else {
      resolved.FB_Kopfposition_Y = 0.0
    }

    if (msg.FB_Kopfposition_X !== undefined) {
      resolved.FB_Kopfposition_X = msg.FB_Kopfposition_X;
    }
    else {
      resolved.FB_Kopfposition_X = 0.0
    }

    return resolved;
    }
};

module.exports = FB_05_Msg;
