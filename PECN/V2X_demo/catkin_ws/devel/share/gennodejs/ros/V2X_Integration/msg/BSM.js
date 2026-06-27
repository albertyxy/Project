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

class BSM {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.id = null;
      this.sec_mark = null;
      this.message_count = null;
      this.latitude = null;
      this.longtitude = null;
      this.elevation = null;
      this.pos_accuracy_semi_major = null;
      this.pos_accuracy_semi_minor = null;
      this.pos_accuracy_orientation = null;
      this.lateral_acceleration = null;
      this.longitudinal_acceleration = null;
      this.vert_acceleration = null;
      this.yaw_acceleration = null;
      this.transmission_state = null;
      this.response_type = null;
      this.light_use = null;
      this.siren_use = null;
      this.events = null;
      this.lights = null;
      this.confidence_position = null;
      this.confidence_elevation = null;
      this.vehicle_class = null;
      this.vehicle_fuel_type = null;
      this.heading = null;
      this.speed = null;
      this.angle = null;
      this.vehicle_width = null;
      this.vehicle_lenth = null;
      this.vehicle_height = null;
      this.brake_padel = null;
      this.wheel_brakes = null;
      this.traction = null;
      this.abs = null;
      this.scs = null;
      this.brake_boost = null;
      this.aux_brakes = null;
    }
    else {
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = '';
      }
      if (initObj.hasOwnProperty('sec_mark')) {
        this.sec_mark = initObj.sec_mark
      }
      else {
        this.sec_mark = 0.0;
      }
      if (initObj.hasOwnProperty('message_count')) {
        this.message_count = initObj.message_count
      }
      else {
        this.message_count = 0;
      }
      if (initObj.hasOwnProperty('latitude')) {
        this.latitude = initObj.latitude
      }
      else {
        this.latitude = 0.0;
      }
      if (initObj.hasOwnProperty('longtitude')) {
        this.longtitude = initObj.longtitude
      }
      else {
        this.longtitude = 0.0;
      }
      if (initObj.hasOwnProperty('elevation')) {
        this.elevation = initObj.elevation
      }
      else {
        this.elevation = 0.0;
      }
      if (initObj.hasOwnProperty('pos_accuracy_semi_major')) {
        this.pos_accuracy_semi_major = initObj.pos_accuracy_semi_major
      }
      else {
        this.pos_accuracy_semi_major = 0.0;
      }
      if (initObj.hasOwnProperty('pos_accuracy_semi_minor')) {
        this.pos_accuracy_semi_minor = initObj.pos_accuracy_semi_minor
      }
      else {
        this.pos_accuracy_semi_minor = 0.0;
      }
      if (initObj.hasOwnProperty('pos_accuracy_orientation')) {
        this.pos_accuracy_orientation = initObj.pos_accuracy_orientation
      }
      else {
        this.pos_accuracy_orientation = 0.0;
      }
      if (initObj.hasOwnProperty('lateral_acceleration')) {
        this.lateral_acceleration = initObj.lateral_acceleration
      }
      else {
        this.lateral_acceleration = 0.0;
      }
      if (initObj.hasOwnProperty('longitudinal_acceleration')) {
        this.longitudinal_acceleration = initObj.longitudinal_acceleration
      }
      else {
        this.longitudinal_acceleration = 0.0;
      }
      if (initObj.hasOwnProperty('vert_acceleration')) {
        this.vert_acceleration = initObj.vert_acceleration
      }
      else {
        this.vert_acceleration = 0.0;
      }
      if (initObj.hasOwnProperty('yaw_acceleration')) {
        this.yaw_acceleration = initObj.yaw_acceleration
      }
      else {
        this.yaw_acceleration = 0.0;
      }
      if (initObj.hasOwnProperty('transmission_state')) {
        this.transmission_state = initObj.transmission_state
      }
      else {
        this.transmission_state = 0;
      }
      if (initObj.hasOwnProperty('response_type')) {
        this.response_type = initObj.response_type
      }
      else {
        this.response_type = 0;
      }
      if (initObj.hasOwnProperty('light_use')) {
        this.light_use = initObj.light_use
      }
      else {
        this.light_use = 0;
      }
      if (initObj.hasOwnProperty('siren_use')) {
        this.siren_use = initObj.siren_use
      }
      else {
        this.siren_use = 0;
      }
      if (initObj.hasOwnProperty('events')) {
        this.events = initObj.events
      }
      else {
        this.events = 0;
      }
      if (initObj.hasOwnProperty('lights')) {
        this.lights = initObj.lights
      }
      else {
        this.lights = 0;
      }
      if (initObj.hasOwnProperty('confidence_position')) {
        this.confidence_position = initObj.confidence_position
      }
      else {
        this.confidence_position = 0;
      }
      if (initObj.hasOwnProperty('confidence_elevation')) {
        this.confidence_elevation = initObj.confidence_elevation
      }
      else {
        this.confidence_elevation = 0;
      }
      if (initObj.hasOwnProperty('vehicle_class')) {
        this.vehicle_class = initObj.vehicle_class
      }
      else {
        this.vehicle_class = 0;
      }
      if (initObj.hasOwnProperty('vehicle_fuel_type')) {
        this.vehicle_fuel_type = initObj.vehicle_fuel_type
      }
      else {
        this.vehicle_fuel_type = 0;
      }
      if (initObj.hasOwnProperty('heading')) {
        this.heading = initObj.heading
      }
      else {
        this.heading = 0.0;
      }
      if (initObj.hasOwnProperty('speed')) {
        this.speed = initObj.speed
      }
      else {
        this.speed = 0.0;
      }
      if (initObj.hasOwnProperty('angle')) {
        this.angle = initObj.angle
      }
      else {
        this.angle = 0;
      }
      if (initObj.hasOwnProperty('vehicle_width')) {
        this.vehicle_width = initObj.vehicle_width
      }
      else {
        this.vehicle_width = 0.0;
      }
      if (initObj.hasOwnProperty('vehicle_lenth')) {
        this.vehicle_lenth = initObj.vehicle_lenth
      }
      else {
        this.vehicle_lenth = 0.0;
      }
      if (initObj.hasOwnProperty('vehicle_height')) {
        this.vehicle_height = initObj.vehicle_height
      }
      else {
        this.vehicle_height = 0.0;
      }
      if (initObj.hasOwnProperty('brake_padel')) {
        this.brake_padel = initObj.brake_padel
      }
      else {
        this.brake_padel = 0;
      }
      if (initObj.hasOwnProperty('wheel_brakes')) {
        this.wheel_brakes = initObj.wheel_brakes
      }
      else {
        this.wheel_brakes = 0;
      }
      if (initObj.hasOwnProperty('traction')) {
        this.traction = initObj.traction
      }
      else {
        this.traction = 0;
      }
      if (initObj.hasOwnProperty('abs')) {
        this.abs = initObj.abs
      }
      else {
        this.abs = 0;
      }
      if (initObj.hasOwnProperty('scs')) {
        this.scs = initObj.scs
      }
      else {
        this.scs = 0;
      }
      if (initObj.hasOwnProperty('brake_boost')) {
        this.brake_boost = initObj.brake_boost
      }
      else {
        this.brake_boost = 0;
      }
      if (initObj.hasOwnProperty('aux_brakes')) {
        this.aux_brakes = initObj.aux_brakes
      }
      else {
        this.aux_brakes = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type BSM
    // Serialize message field [id]
    bufferOffset = _serializer.string(obj.id, buffer, bufferOffset);
    // Serialize message field [sec_mark]
    bufferOffset = _serializer.float32(obj.sec_mark, buffer, bufferOffset);
    // Serialize message field [message_count]
    bufferOffset = _serializer.int16(obj.message_count, buffer, bufferOffset);
    // Serialize message field [latitude]
    bufferOffset = _serializer.float32(obj.latitude, buffer, bufferOffset);
    // Serialize message field [longtitude]
    bufferOffset = _serializer.float32(obj.longtitude, buffer, bufferOffset);
    // Serialize message field [elevation]
    bufferOffset = _serializer.float32(obj.elevation, buffer, bufferOffset);
    // Serialize message field [pos_accuracy_semi_major]
    bufferOffset = _serializer.float32(obj.pos_accuracy_semi_major, buffer, bufferOffset);
    // Serialize message field [pos_accuracy_semi_minor]
    bufferOffset = _serializer.float32(obj.pos_accuracy_semi_minor, buffer, bufferOffset);
    // Serialize message field [pos_accuracy_orientation]
    bufferOffset = _serializer.float32(obj.pos_accuracy_orientation, buffer, bufferOffset);
    // Serialize message field [lateral_acceleration]
    bufferOffset = _serializer.float32(obj.lateral_acceleration, buffer, bufferOffset);
    // Serialize message field [longitudinal_acceleration]
    bufferOffset = _serializer.float32(obj.longitudinal_acceleration, buffer, bufferOffset);
    // Serialize message field [vert_acceleration]
    bufferOffset = _serializer.float32(obj.vert_acceleration, buffer, bufferOffset);
    // Serialize message field [yaw_acceleration]
    bufferOffset = _serializer.float32(obj.yaw_acceleration, buffer, bufferOffset);
    // Serialize message field [transmission_state]
    bufferOffset = _serializer.uint8(obj.transmission_state, buffer, bufferOffset);
    // Serialize message field [response_type]
    bufferOffset = _serializer.uint8(obj.response_type, buffer, bufferOffset);
    // Serialize message field [light_use]
    bufferOffset = _serializer.uint8(obj.light_use, buffer, bufferOffset);
    // Serialize message field [siren_use]
    bufferOffset = _serializer.uint8(obj.siren_use, buffer, bufferOffset);
    // Serialize message field [events]
    bufferOffset = _serializer.uint8(obj.events, buffer, bufferOffset);
    // Serialize message field [lights]
    bufferOffset = _serializer.uint8(obj.lights, buffer, bufferOffset);
    // Serialize message field [confidence_position]
    bufferOffset = _serializer.uint8(obj.confidence_position, buffer, bufferOffset);
    // Serialize message field [confidence_elevation]
    bufferOffset = _serializer.uint8(obj.confidence_elevation, buffer, bufferOffset);
    // Serialize message field [vehicle_class]
    bufferOffset = _serializer.uint8(obj.vehicle_class, buffer, bufferOffset);
    // Serialize message field [vehicle_fuel_type]
    bufferOffset = _serializer.uint8(obj.vehicle_fuel_type, buffer, bufferOffset);
    // Serialize message field [heading]
    bufferOffset = _serializer.float32(obj.heading, buffer, bufferOffset);
    // Serialize message field [speed]
    bufferOffset = _serializer.float32(obj.speed, buffer, bufferOffset);
    // Serialize message field [angle]
    bufferOffset = _serializer.int16(obj.angle, buffer, bufferOffset);
    // Serialize message field [vehicle_width]
    bufferOffset = _serializer.float32(obj.vehicle_width, buffer, bufferOffset);
    // Serialize message field [vehicle_lenth]
    bufferOffset = _serializer.float32(obj.vehicle_lenth, buffer, bufferOffset);
    // Serialize message field [vehicle_height]
    bufferOffset = _serializer.float32(obj.vehicle_height, buffer, bufferOffset);
    // Serialize message field [brake_padel]
    bufferOffset = _serializer.uint8(obj.brake_padel, buffer, bufferOffset);
    // Serialize message field [wheel_brakes]
    bufferOffset = _serializer.uint8(obj.wheel_brakes, buffer, bufferOffset);
    // Serialize message field [traction]
    bufferOffset = _serializer.uint8(obj.traction, buffer, bufferOffset);
    // Serialize message field [abs]
    bufferOffset = _serializer.uint8(obj.abs, buffer, bufferOffset);
    // Serialize message field [scs]
    bufferOffset = _serializer.uint8(obj.scs, buffer, bufferOffset);
    // Serialize message field [brake_boost]
    bufferOffset = _serializer.uint8(obj.brake_boost, buffer, bufferOffset);
    // Serialize message field [aux_brakes]
    bufferOffset = _serializer.uint8(obj.aux_brakes, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type BSM
    let len;
    let data = new BSM(null);
    // Deserialize message field [id]
    data.id = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [sec_mark]
    data.sec_mark = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [message_count]
    data.message_count = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [latitude]
    data.latitude = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [longtitude]
    data.longtitude = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [elevation]
    data.elevation = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [pos_accuracy_semi_major]
    data.pos_accuracy_semi_major = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [pos_accuracy_semi_minor]
    data.pos_accuracy_semi_minor = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [pos_accuracy_orientation]
    data.pos_accuracy_orientation = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [lateral_acceleration]
    data.lateral_acceleration = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [longitudinal_acceleration]
    data.longitudinal_acceleration = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [vert_acceleration]
    data.vert_acceleration = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [yaw_acceleration]
    data.yaw_acceleration = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [transmission_state]
    data.transmission_state = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [response_type]
    data.response_type = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [light_use]
    data.light_use = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [siren_use]
    data.siren_use = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [events]
    data.events = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [lights]
    data.lights = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [confidence_position]
    data.confidence_position = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [confidence_elevation]
    data.confidence_elevation = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [vehicle_class]
    data.vehicle_class = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [vehicle_fuel_type]
    data.vehicle_fuel_type = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [heading]
    data.heading = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [speed]
    data.speed = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [angle]
    data.angle = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [vehicle_width]
    data.vehicle_width = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [vehicle_lenth]
    data.vehicle_lenth = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [vehicle_height]
    data.vehicle_height = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [brake_padel]
    data.brake_padel = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [wheel_brakes]
    data.wheel_brakes = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [traction]
    data.traction = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [abs]
    data.abs = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [scs]
    data.scs = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [brake_boost]
    data.brake_boost = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [aux_brakes]
    data.aux_brakes = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.id.length;
    return length + 89;
  }

  static datatype() {
    // Returns string type for a message object
    return 'V2X_Integration/BSM';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e6940b8bdce7382d047211cc39f10e12';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string id
    float32 sec_mark
    int16 message_count
    float32 latitude
    float32 longtitude
    float32 elevation
    float32 pos_accuracy_semi_major
    float32 pos_accuracy_semi_minor
    float32 pos_accuracy_orientation
    float32 lateral_acceleration
    float32 longitudinal_acceleration
    float32 vert_acceleration
    float32 yaw_acceleration
    uint8 transmission_state
    uint8 response_type
    uint8 light_use
    uint8 siren_use
    uint8 events
    uint8 lights
    uint8 confidence_position
    uint8 confidence_elevation
    uint8 vehicle_class
    uint8 vehicle_fuel_type
    float32 heading
    float32 speed
    int16 angle
    float32 vehicle_width
    float32 vehicle_lenth
    float32 vehicle_height
    uint8 brake_padel
    uint8 wheel_brakes
    uint8 traction
    uint8 abs
    uint8 scs
    uint8 brake_boost
    uint8 aux_brakes
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new BSM(null);
    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = ''
    }

    if (msg.sec_mark !== undefined) {
      resolved.sec_mark = msg.sec_mark;
    }
    else {
      resolved.sec_mark = 0.0
    }

    if (msg.message_count !== undefined) {
      resolved.message_count = msg.message_count;
    }
    else {
      resolved.message_count = 0
    }

    if (msg.latitude !== undefined) {
      resolved.latitude = msg.latitude;
    }
    else {
      resolved.latitude = 0.0
    }

    if (msg.longtitude !== undefined) {
      resolved.longtitude = msg.longtitude;
    }
    else {
      resolved.longtitude = 0.0
    }

    if (msg.elevation !== undefined) {
      resolved.elevation = msg.elevation;
    }
    else {
      resolved.elevation = 0.0
    }

    if (msg.pos_accuracy_semi_major !== undefined) {
      resolved.pos_accuracy_semi_major = msg.pos_accuracy_semi_major;
    }
    else {
      resolved.pos_accuracy_semi_major = 0.0
    }

    if (msg.pos_accuracy_semi_minor !== undefined) {
      resolved.pos_accuracy_semi_minor = msg.pos_accuracy_semi_minor;
    }
    else {
      resolved.pos_accuracy_semi_minor = 0.0
    }

    if (msg.pos_accuracy_orientation !== undefined) {
      resolved.pos_accuracy_orientation = msg.pos_accuracy_orientation;
    }
    else {
      resolved.pos_accuracy_orientation = 0.0
    }

    if (msg.lateral_acceleration !== undefined) {
      resolved.lateral_acceleration = msg.lateral_acceleration;
    }
    else {
      resolved.lateral_acceleration = 0.0
    }

    if (msg.longitudinal_acceleration !== undefined) {
      resolved.longitudinal_acceleration = msg.longitudinal_acceleration;
    }
    else {
      resolved.longitudinal_acceleration = 0.0
    }

    if (msg.vert_acceleration !== undefined) {
      resolved.vert_acceleration = msg.vert_acceleration;
    }
    else {
      resolved.vert_acceleration = 0.0
    }

    if (msg.yaw_acceleration !== undefined) {
      resolved.yaw_acceleration = msg.yaw_acceleration;
    }
    else {
      resolved.yaw_acceleration = 0.0
    }

    if (msg.transmission_state !== undefined) {
      resolved.transmission_state = msg.transmission_state;
    }
    else {
      resolved.transmission_state = 0
    }

    if (msg.response_type !== undefined) {
      resolved.response_type = msg.response_type;
    }
    else {
      resolved.response_type = 0
    }

    if (msg.light_use !== undefined) {
      resolved.light_use = msg.light_use;
    }
    else {
      resolved.light_use = 0
    }

    if (msg.siren_use !== undefined) {
      resolved.siren_use = msg.siren_use;
    }
    else {
      resolved.siren_use = 0
    }

    if (msg.events !== undefined) {
      resolved.events = msg.events;
    }
    else {
      resolved.events = 0
    }

    if (msg.lights !== undefined) {
      resolved.lights = msg.lights;
    }
    else {
      resolved.lights = 0
    }

    if (msg.confidence_position !== undefined) {
      resolved.confidence_position = msg.confidence_position;
    }
    else {
      resolved.confidence_position = 0
    }

    if (msg.confidence_elevation !== undefined) {
      resolved.confidence_elevation = msg.confidence_elevation;
    }
    else {
      resolved.confidence_elevation = 0
    }

    if (msg.vehicle_class !== undefined) {
      resolved.vehicle_class = msg.vehicle_class;
    }
    else {
      resolved.vehicle_class = 0
    }

    if (msg.vehicle_fuel_type !== undefined) {
      resolved.vehicle_fuel_type = msg.vehicle_fuel_type;
    }
    else {
      resolved.vehicle_fuel_type = 0
    }

    if (msg.heading !== undefined) {
      resolved.heading = msg.heading;
    }
    else {
      resolved.heading = 0.0
    }

    if (msg.speed !== undefined) {
      resolved.speed = msg.speed;
    }
    else {
      resolved.speed = 0.0
    }

    if (msg.angle !== undefined) {
      resolved.angle = msg.angle;
    }
    else {
      resolved.angle = 0
    }

    if (msg.vehicle_width !== undefined) {
      resolved.vehicle_width = msg.vehicle_width;
    }
    else {
      resolved.vehicle_width = 0.0
    }

    if (msg.vehicle_lenth !== undefined) {
      resolved.vehicle_lenth = msg.vehicle_lenth;
    }
    else {
      resolved.vehicle_lenth = 0.0
    }

    if (msg.vehicle_height !== undefined) {
      resolved.vehicle_height = msg.vehicle_height;
    }
    else {
      resolved.vehicle_height = 0.0
    }

    if (msg.brake_padel !== undefined) {
      resolved.brake_padel = msg.brake_padel;
    }
    else {
      resolved.brake_padel = 0
    }

    if (msg.wheel_brakes !== undefined) {
      resolved.wheel_brakes = msg.wheel_brakes;
    }
    else {
      resolved.wheel_brakes = 0
    }

    if (msg.traction !== undefined) {
      resolved.traction = msg.traction;
    }
    else {
      resolved.traction = 0
    }

    if (msg.abs !== undefined) {
      resolved.abs = msg.abs;
    }
    else {
      resolved.abs = 0
    }

    if (msg.scs !== undefined) {
      resolved.scs = msg.scs;
    }
    else {
      resolved.scs = 0
    }

    if (msg.brake_boost !== undefined) {
      resolved.brake_boost = msg.brake_boost;
    }
    else {
      resolved.brake_boost = 0
    }

    if (msg.aux_brakes !== undefined) {
      resolved.aux_brakes = msg.aux_brakes;
    }
    else {
      resolved.aux_brakes = 0
    }

    return resolved;
    }
};

module.exports = BSM;
