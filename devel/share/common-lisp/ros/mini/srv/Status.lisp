; Auto-generated. Do not edit!


(cl:in-package mini-srv)


;//! \htmlinclude Status-request.msg.html

(cl:defclass <Status-request> (roslisp-msg-protocol:ros-message)
  ((get_status
    :reader get_status
    :initarg :get_status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Status-request (<Status-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Status-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Status-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mini-srv:<Status-request> is deprecated: use mini-srv:Status-request instead.")))

(cl:ensure-generic-function 'get_status-val :lambda-list '(m))
(cl:defmethod get_status-val ((m <Status-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mini-srv:get_status-val is deprecated.  Use mini-srv:get_status instead.")
  (get_status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Status-request>) ostream)
  "Serializes a message object of type '<Status-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'get_status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Status-request>) istream)
  "Deserializes a message object of type '<Status-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'get_status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Status-request>)))
  "Returns string type for a service object of type '<Status-request>"
  "mini/StatusRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Status-request)))
  "Returns string type for a service object of type 'Status-request"
  "mini/StatusRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Status-request>)))
  "Returns md5sum for a message object of type '<Status-request>"
  "b594a92c01db0a8232b059d768ace0a2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Status-request)))
  "Returns md5sum for a message object of type 'Status-request"
  "b594a92c01db0a8232b059d768ace0a2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Status-request>)))
  "Returns full string definition for message of type '<Status-request>"
  (cl:format cl:nil "# Possible values for get_status~%# uint8 GET_STATUS_VEHICLE_STATE = 0~%# uint8 GET_STATUS_CONTROL_MODE = 1~%# uint8 GET_STATUS_BATTERY_VOLTAGE = 2~%# uint8 GET_STATUS_ERROR_CODE = 3~%# uint8 GET_STATUS_MOTION_MODE = 4~%~%# request~%uint8 get_status~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Status-request)))
  "Returns full string definition for message of type 'Status-request"
  (cl:format cl:nil "# Possible values for get_status~%# uint8 GET_STATUS_VEHICLE_STATE = 0~%# uint8 GET_STATUS_CONTROL_MODE = 1~%# uint8 GET_STATUS_BATTERY_VOLTAGE = 2~%# uint8 GET_STATUS_ERROR_CODE = 3~%# uint8 GET_STATUS_MOTION_MODE = 4~%~%# request~%uint8 get_status~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Status-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Status-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Status-request
    (cl:cons ':get_status (get_status msg))
))
;//! \htmlinclude Status-response.msg.html

(cl:defclass <Status-response> (roslisp-msg-protocol:ros-message)
  ((status_string
    :reader status_string
    :initarg :status_string
    :type cl:string
    :initform ""))
)

(cl:defclass Status-response (<Status-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Status-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Status-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mini-srv:<Status-response> is deprecated: use mini-srv:Status-response instead.")))

(cl:ensure-generic-function 'status_string-val :lambda-list '(m))
(cl:defmethod status_string-val ((m <Status-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mini-srv:status_string-val is deprecated.  Use mini-srv:status_string instead.")
  (status_string m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Status-response>) ostream)
  "Serializes a message object of type '<Status-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'status_string))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'status_string))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Status-response>) istream)
  "Deserializes a message object of type '<Status-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'status_string) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'status_string) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Status-response>)))
  "Returns string type for a service object of type '<Status-response>"
  "mini/StatusResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Status-response)))
  "Returns string type for a service object of type 'Status-response"
  "mini/StatusResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Status-response>)))
  "Returns md5sum for a message object of type '<Status-response>"
  "b594a92c01db0a8232b059d768ace0a2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Status-response)))
  "Returns md5sum for a message object of type 'Status-response"
  "b594a92c01db0a8232b059d768ace0a2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Status-response>)))
  "Returns full string definition for message of type '<Status-response>"
  (cl:format cl:nil "# response~%string status_string~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Status-response)))
  "Returns full string definition for message of type 'Status-response"
  (cl:format cl:nil "# response~%string status_string~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Status-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'status_string))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Status-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Status-response
    (cl:cons ':status_string (status_string msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Status)))
  'Status-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Status)))
  'Status-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Status)))
  "Returns string type for a service object of type '<Status>"
  "mini/Status")