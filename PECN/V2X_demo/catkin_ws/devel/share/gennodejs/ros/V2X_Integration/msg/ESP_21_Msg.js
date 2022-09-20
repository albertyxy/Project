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

class ESP_21_Msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.ESP_21_CRC = null;
      this.ESP_21_BZ = null;
      this.BR_Eingriffsmoment = null;
      this.ESP_Diagnose = null;
      this.ESC_v_Signal_Qualifier_High_Low = null;
      this.ESP_Vorsteuerung = null;
      this.OBD_Schlechtweg = null;
      this.OBD_QBit_Schlechtweg = null;
      this.ESP_v_Signal = null;
      this.ASR_Tastung_passiv = null;
      this.ESP_Tastung_passiv = null;
      this.ESP_Systemstatus = null;
      this.ASR_Schalteingriff = null;
      this.ESP_QBit_v_Signal = null;
      this.ABS_Bremsung = null;
      this.ASR_Anf = null;
      this.MSR_Anf = null;
      this.EBV_Eingriff = null;
      this.EDS_Eingriff = null;
      this.ESP_Eingriff = null;
      this.ESP_ASP = null;
      this.ESC_Neutralschaltung = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('ESP_21_CRC')) {
        this.ESP_21_CRC = initObj.ESP_21_CRC
      }
      else {
        this.ESP_21_CRC = 0;
      }
      if (initObj.hasOwnProperty('ESP_21_BZ')) {
        this.ESP_21_BZ = initObj.ESP_21_BZ
      }
      else {
        this.ESP_21_BZ = 0;
      }
      if (initObj.hasOwnProperty('BR_Eingriffsmoment')) {
        this.BR_Eingriffsmoment = initObj.BR_Eingriffsmoment
      }
      else {
        this.BR_Eingriffsmoment = 0;
      }
      if (initObj.hasOwnProperty('ESP_Diagnose')) {
        this.ESP_Diagnose = initObj.ESP_Diagnose
      }
      else {
        this.ESP_Diagnose = 0;
      }
      if (initObj.hasOwnProperty('ESC_v_Signal_Qualifier_High_Low')) {
        this.ESC_v_Signal_Qualifier_High_Low = initObj.ESC_v_Signal_Qualifier_High_Low
      }
      else {
        this.ESC_v_Signal_Qualifier_High_Low = 0;
      }
      if (initObj.hasOwnProperty('ESP_Vorsteuerung')) {
        this.ESP_Vorsteuerung = initObj.ESP_Vorsteuerung
      }
      else {
        this.ESP_Vorsteuerung = 0;
      }
      if (initObj.hasOwnProperty('OBD_Schlechtweg')) {
        this.OBD_Schlechtweg = initObj.OBD_Schlechtweg
      }
      else {
        this.OBD_Schlechtweg = 0;
      }
      if (initObj.hasOwnProperty('OBD_QBit_Schlechtweg')) {
        this.OBD_QBit_Schlechtweg = initObj.OBD_QBit_Schlechtweg
      }
      else {
        this.OBD_QBit_Schlechtweg = 0;
      }
      if (initObj.hasOwnProperty('ESP_v_Signal')) {
        this.ESP_v_Signal = initObj.ESP_v_Signal
      }
      else {
        this.ESP_v_Signal = 0.0;
      }
      if (initObj.hasOwnProperty('ASR_Tastung_passiv')) {
        this.ASR_Tastung_passiv = initObj.ASR_Tastung_passiv
      }
      else {
        this.ASR_Tastung_passiv = 0;
      }
      if (initObj.hasOwnProperty('ESP_Tastung_passiv')) {
        this.ESP_Tastung_passiv = initObj.ESP_Tastung_passiv
      }
      else {
        this.ESP_Tastung_passiv = 0;
      }
      if (initObj.hasOwnProperty('ESP_Systemstatus')) {
        this.ESP_Systemstatus = initObj.ESP_Systemstatus
      }
      else {
        this.ESP_Systemstatus = 0;
      }
      if (initObj.hasOwnProperty('ASR_Schalteingriff')) {
        this.ASR_Schalteingriff = initObj.ASR_Schalteingriff
      }
      else {
        this.ASR_Schalteingriff = 0;
      }
      if (initObj.hasOwnProperty('ESP_QBit_v_Signal')) {
        this.ESP_QBit_v_Signal = initObj.ESP_QBit_v_Signal
      }
      else {
        this.ESP_QBit_v_Signal = 0;
      }
      if (initObj.hasOwnProperty('ABS_Bremsung')) {
        this.ABS_Bremsung = initObj.ABS_Bremsung
      }
      else {
        this.ABS_Bremsung = 0;
      }
      if (initObj.hasOwnProperty('ASR_Anf')) {
        this.ASR_Anf = initObj.ASR_Anf
      }
      else {
        this.ASR_Anf = 0;
      }
      if (initObj.hasOwnProperty('MSR_Anf')) {
        this.MSR_Anf = initObj.MSR_Anf
      }
      else {
        this.MSR_Anf = 0;
      }
      if (initObj.hasOwnProperty('EBV_Eingriff')) {
        this.EBV_Eingriff = initObj.EBV_Eingriff
      }
      else {
        this.EBV_Eingriff = 0;
      }
      if (initObj.hasOwnProperty('EDS_Eingriff')) {
        this.EDS_Eingriff = initObj.EDS_Eingriff
      }
      else {
        this.EDS_Eingriff = 0;
      }
      if (initObj.hasOwnProperty('ESP_Eingriff')) {
        this.ESP_Eingriff = initObj.ESP_Eingriff
      }
      else {
        this.ESP_Eingriff = 0;
      }
      if (initObj.hasOwnProperty('ESP_ASP')) {
        this.ESP_ASP = initObj.ESP_ASP
      }
      else {
        this.ESP_ASP = 0;
      }
      if (initObj.hasOwnProperty('ESC_Neutralschaltung')) {
        this.ESC_Neutralschaltung = initObj.ESC_Neutralschaltung
      }
      else {
        this.ESC_Neutralschaltung = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ESP_21_Msg
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [ESP_21_CRC]
    bufferOffset = _serializer.uint16(obj.ESP_21_CRC, buffer, bufferOffset);
    // Serialize message field [ESP_21_BZ]
    bufferOffset = _serializer.uint8(obj.ESP_21_BZ, buffer, bufferOffset);
    // Serialize message field [BR_Eingriffsmoment]
    bufferOffset = _serializer.int16(obj.BR_Eingriffsmoment, buffer, bufferOffset);
    // Serialize message field [ESP_Diagnose]
    bufferOffset = _serializer.uint8(obj.ESP_Diagnose, buffer, bufferOffset);
    // Serialize message field [ESC_v_Signal_Qualifier_High_Low]
    bufferOffset = _serializer.uint8(obj.ESC_v_Signal_Qualifier_High_Low, buffer, bufferOffset);
    // Serialize message field [ESP_Vorsteuerung]
    bufferOffset = _serializer.uint8(obj.ESP_Vorsteuerung, buffer, bufferOffset);
    // Serialize message field [OBD_Schlechtweg]
    bufferOffset = _serializer.uint8(obj.OBD_Schlechtweg, buffer, bufferOffset);
    // Serialize message field [OBD_QBit_Schlechtweg]
    bufferOffset = _serializer.uint8(obj.OBD_QBit_Schlechtweg, buffer, bufferOffset);
    // Serialize message field [ESP_v_Signal]
    bufferOffset = _serializer.float32(obj.ESP_v_Signal, buffer, bufferOffset);
    // Serialize message field [ASR_Tastung_passiv]
    bufferOffset = _serializer.uint8(obj.ASR_Tastung_passiv, buffer, bufferOffset);
    // Serialize message field [ESP_Tastung_passiv]
    bufferOffset = _serializer.uint8(obj.ESP_Tastung_passiv, buffer, bufferOffset);
    // Serialize message field [ESP_Systemstatus]
    bufferOffset = _serializer.uint8(obj.ESP_Systemstatus, buffer, bufferOffset);
    // Serialize message field [ASR_Schalteingriff]
    bufferOffset = _serializer.uint8(obj.ASR_Schalteingriff, buffer, bufferOffset);
    // Serialize message field [ESP_QBit_v_Signal]
    bufferOffset = _serializer.uint8(obj.ESP_QBit_v_Signal, buffer, bufferOffset);
    // Serialize message field [ABS_Bremsung]
    bufferOffset = _serializer.uint8(obj.ABS_Bremsung, buffer, bufferOffset);
    // Serialize message field [ASR_Anf]
    bufferOffset = _serializer.uint8(obj.ASR_Anf, buffer, bufferOffset);
    // Serialize message field [MSR_Anf]
    bufferOffset = _serializer.uint8(obj.MSR_Anf, buffer, bufferOffset);
    // Serialize message field [EBV_Eingriff]
    bufferOffset = _serializer.uint8(obj.EBV_Eingriff, buffer, bufferOffset);
    // Serialize message field [EDS_Eingriff]
    bufferOffset = _serializer.uint8(obj.EDS_Eingriff, buffer, bufferOffset);
    // Serialize message field [ESP_Eingriff]
    bufferOffset = _serializer.uint8(obj.ESP_Eingriff, buffer, bufferOffset);
    // Serialize message field [ESP_ASP]
    bufferOffset = _serializer.uint8(obj.ESP_ASP, buffer, bufferOffset);
    // Serialize message field [ESC_Neutralschaltung]
    bufferOffset = _serializer.uint8(obj.ESC_Neutralschaltung, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ESP_21_Msg
    let len;
    let data = new ESP_21_Msg(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [ESP_21_CRC]
    data.ESP_21_CRC = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [ESP_21_BZ]
    data.ESP_21_BZ = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [BR_Eingriffsmoment]
    data.BR_Eingriffsmoment = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [ESP_Diagnose]
    data.ESP_Diagnose = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ESC_v_Signal_Qualifier_High_Low]
    data.ESC_v_Signal_Qualifier_High_Low = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ESP_Vorsteuerung]
    data.ESP_Vorsteuerung = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [OBD_Schlechtweg]
    data.OBD_Schlechtweg = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [OBD_QBit_Schlechtweg]
    data.OBD_QBit_Schlechtweg = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ESP_v_Signal]
    data.ESP_v_Signal = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [ASR_Tastung_passiv]
    data.ASR_Tastung_passiv = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ESP_Tastung_passiv]
    data.ESP_Tastung_passiv = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ESP_Systemstatus]
    data.ESP_Systemstatus = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ASR_Schalteingriff]
    data.ASR_Schalteingriff = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ESP_QBit_v_Signal]
    data.ESP_QBit_v_Signal = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ABS_Bremsung]
    data.ABS_Bremsung = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ASR_Anf]
    data.ASR_Anf = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [MSR_Anf]
    data.MSR_Anf = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [EBV_Eingriff]
    data.EBV_Eingriff = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [EDS_Eingriff]
    data.EDS_Eingriff = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ESP_Eingriff]
    data.ESP_Eingriff = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ESP_ASP]
    data.ESP_ASP = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ESC_Neutralschaltung]
    data.ESC_Neutralschaltung = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 27;
  }

  static datatype() {
    // Returns string type for a message object
    return 'V2X_Integration/ESP_21_Msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '14034e15be32d792bb36bad51c5aaa1b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ESP_21_Msg(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.ESP_21_CRC !== undefined) {
      resolved.ESP_21_CRC = msg.ESP_21_CRC;
    }
    else {
      resolved.ESP_21_CRC = 0
    }

    if (msg.ESP_21_BZ !== undefined) {
      resolved.ESP_21_BZ = msg.ESP_21_BZ;
    }
    else {
      resolved.ESP_21_BZ = 0
    }

    if (msg.BR_Eingriffsmoment !== undefined) {
      resolved.BR_Eingriffsmoment = msg.BR_Eingriffsmoment;
    }
    else {
      resolved.BR_Eingriffsmoment = 0
    }

    if (msg.ESP_Diagnose !== undefined) {
      resolved.ESP_Diagnose = msg.ESP_Diagnose;
    }
    else {
      resolved.ESP_Diagnose = 0
    }

    if (msg.ESC_v_Signal_Qualifier_High_Low !== undefined) {
      resolved.ESC_v_Signal_Qualifier_High_Low = msg.ESC_v_Signal_Qualifier_High_Low;
    }
    else {
      resolved.ESC_v_Signal_Qualifier_High_Low = 0
    }

    if (msg.ESP_Vorsteuerung !== undefined) {
      resolved.ESP_Vorsteuerung = msg.ESP_Vorsteuerung;
    }
    else {
      resolved.ESP_Vorsteuerung = 0
    }

    if (msg.OBD_Schlechtweg !== undefined) {
      resolved.OBD_Schlechtweg = msg.OBD_Schlechtweg;
    }
    else {
      resolved.OBD_Schlechtweg = 0
    }

    if (msg.OBD_QBit_Schlechtweg !== undefined) {
      resolved.OBD_QBit_Schlechtweg = msg.OBD_QBit_Schlechtweg;
    }
    else {
      resolved.OBD_QBit_Schlechtweg = 0
    }

    if (msg.ESP_v_Signal !== undefined) {
      resolved.ESP_v_Signal = msg.ESP_v_Signal;
    }
    else {
      resolved.ESP_v_Signal = 0.0
    }

    if (msg.ASR_Tastung_passiv !== undefined) {
      resolved.ASR_Tastung_passiv = msg.ASR_Tastung_passiv;
    }
    else {
      resolved.ASR_Tastung_passiv = 0
    }

    if (msg.ESP_Tastung_passiv !== undefined) {
      resolved.ESP_Tastung_passiv = msg.ESP_Tastung_passiv;
    }
    else {
      resolved.ESP_Tastung_passiv = 0
    }

    if (msg.ESP_Systemstatus !== undefined) {
      resolved.ESP_Systemstatus = msg.ESP_Systemstatus;
    }
    else {
      resolved.ESP_Systemstatus = 0
    }

    if (msg.ASR_Schalteingriff !== undefined) {
      resolved.ASR_Schalteingriff = msg.ASR_Schalteingriff;
    }
    else {
      resolved.ASR_Schalteingriff = 0
    }

    if (msg.ESP_QBit_v_Signal !== undefined) {
      resolved.ESP_QBit_v_Signal = msg.ESP_QBit_v_Signal;
    }
    else {
      resolved.ESP_QBit_v_Signal = 0
    }

    if (msg.ABS_Bremsung !== undefined) {
      resolved.ABS_Bremsung = msg.ABS_Bremsung;
    }
    else {
      resolved.ABS_Bremsung = 0
    }

    if (msg.ASR_Anf !== undefined) {
      resolved.ASR_Anf = msg.ASR_Anf;
    }
    else {
      resolved.ASR_Anf = 0
    }

    if (msg.MSR_Anf !== undefined) {
      resolved.MSR_Anf = msg.MSR_Anf;
    }
    else {
      resolved.MSR_Anf = 0
    }

    if (msg.EBV_Eingriff !== undefined) {
      resolved.EBV_Eingriff = msg.EBV_Eingriff;
    }
    else {
      resolved.EBV_Eingriff = 0
    }

    if (msg.EDS_Eingriff !== undefined) {
      resolved.EDS_Eingriff = msg.EDS_Eingriff;
    }
    else {
      resolved.EDS_Eingriff = 0
    }

    if (msg.ESP_Eingriff !== undefined) {
      resolved.ESP_Eingriff = msg.ESP_Eingriff;
    }
    else {
      resolved.ESP_Eingriff = 0
    }

    if (msg.ESP_ASP !== undefined) {
      resolved.ESP_ASP = msg.ESP_ASP;
    }
    else {
      resolved.ESP_ASP = 0
    }

    if (msg.ESC_Neutralschaltung !== undefined) {
      resolved.ESC_Neutralschaltung = msg.ESC_Neutralschaltung;
    }
    else {
      resolved.ESC_Neutralschaltung = 0
    }

    return resolved;
    }
};

module.exports = ESP_21_Msg;
