// Auto-generated. Do not edit!

// (in-package mini.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class StatusRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.get_status = null;
    }
    else {
      if (initObj.hasOwnProperty('get_status')) {
        this.get_status = initObj.get_status
      }
      else {
        this.get_status = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type StatusRequest
    // Serialize message field [get_status]
    bufferOffset = _serializer.uint8(obj.get_status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type StatusRequest
    let len;
    let data = new StatusRequest(null);
    // Deserialize message field [get_status]
    data.get_status = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'mini/StatusRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c4dd1aa84b07741a714357c84f9e0c18';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Possible values for get_status
    # uint8 GET_STATUS_VEHICLE_STATE = 0
    # uint8 GET_STATUS_CONTROL_MODE = 1
    # uint8 GET_STATUS_BATTERY_VOLTAGE = 2
    # uint8 GET_STATUS_ERROR_CODE = 3
    # uint8 GET_STATUS_MOTION_MODE = 4
    
    # request
    uint8 get_status
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new StatusRequest(null);
    if (msg.get_status !== undefined) {
      resolved.get_status = msg.get_status;
    }
    else {
      resolved.get_status = 0
    }

    return resolved;
    }
};

class StatusResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.status_string = null;
    }
    else {
      if (initObj.hasOwnProperty('status_string')) {
        this.status_string = initObj.status_string
      }
      else {
        this.status_string = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type StatusResponse
    // Serialize message field [status_string]
    bufferOffset = _serializer.string(obj.status_string, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type StatusResponse
    let len;
    let data = new StatusResponse(null);
    // Deserialize message field [status_string]
    data.status_string = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.status_string.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'mini/StatusResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4c41b913733274581895abeeed69a701';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # response
    string status_string
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new StatusResponse(null);
    if (msg.status_string !== undefined) {
      resolved.status_string = msg.status_string;
    }
    else {
      resolved.status_string = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: StatusRequest,
  Response: StatusResponse,
  md5sum() { return 'b594a92c01db0a8232b059d768ace0a2'; },
  datatype() { return 'mini/Status'; }
};
