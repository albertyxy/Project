; Auto-generated. Do not edit!


(cl:in-package V2X_Integration-msg)


;//! \htmlinclude SARA_06_Msg.msg.html

(cl:defclass <SARA_06_Msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (SARA_06_CRC
    :reader SARA_06_CRC
    :initarg :SARA_06_CRC
    :type cl:fixnum
    :initform 0)
   (SARA_06_BZ
    :reader SARA_06_BZ
    :initarg :SARA_06_BZ
    :type cl:fixnum
    :initform 0)
   (SARA_Accel_X_010
    :reader SARA_Accel_X_010
    :initarg :SARA_Accel_X_010
    :type cl:float
    :initform 0.0)
   (SARA_Accel_Y_010
    :reader SARA_Accel_Y_010
    :initarg :SARA_Accel_Y_010
    :type cl:float
    :initform 0.0)
   (SARA_Omega_Z_010
    :reader SARA_Omega_Z_010
    :initarg :SARA_Omega_Z_010
    :type cl:float
    :initform 0.0)
   (SARA_CF_Accel_X_010
    :reader SARA_CF_Accel_X_010
    :initarg :SARA_CF_Accel_X_010
    :type cl:fixnum
    :initform 0)
   (SARA_CF_Accel_Y_010
    :reader SARA_CF_Accel_Y_010
    :initarg :SARA_CF_Accel_Y_010
    :type cl:fixnum
    :initform 0)
   (SARA_CF_Omega_Z_010
    :reader SARA_CF_Omega_Z_010
    :initarg :SARA_CF_Omega_Z_010
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SARA_06_Msg (<SARA_06_Msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SARA_06_Msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SARA_06_Msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name V2X_Integration-msg:<SARA_06_Msg> is deprecated: use V2X_Integration-msg:SARA_06_Msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <SARA_06_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:header-val is deprecated.  Use V2X_Integration-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'SARA_06_CRC-val :lambda-list '(m))
(cl:defmethod SARA_06_CRC-val ((m <SARA_06_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:SARA_06_CRC-val is deprecated.  Use V2X_Integration-msg:SARA_06_CRC instead.")
  (SARA_06_CRC m))

(cl:ensure-generic-function 'SARA_06_BZ-val :lambda-list '(m))
(cl:defmethod SARA_06_BZ-val ((m <SARA_06_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:SARA_06_BZ-val is deprecated.  Use V2X_Integration-msg:SARA_06_BZ instead.")
  (SARA_06_BZ m))

(cl:ensure-generic-function 'SARA_Accel_X_010-val :lambda-list '(m))
(cl:defmethod SARA_Accel_X_010-val ((m <SARA_06_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:SARA_Accel_X_010-val is deprecated.  Use V2X_Integration-msg:SARA_Accel_X_010 instead.")
  (SARA_Accel_X_010 m))

(cl:ensure-generic-function 'SARA_Accel_Y_010-val :lambda-list '(m))
(cl:defmethod SARA_Accel_Y_010-val ((m <SARA_06_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:SARA_Accel_Y_010-val is deprecated.  Use V2X_Integration-msg:SARA_Accel_Y_010 instead.")
  (SARA_Accel_Y_010 m))

(cl:ensure-generic-function 'SARA_Omega_Z_010-val :lambda-list '(m))
(cl:defmethod SARA_Omega_Z_010-val ((m <SARA_06_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:SARA_Omega_Z_010-val is deprecated.  Use V2X_Integration-msg:SARA_Omega_Z_010 instead.")
  (SARA_Omega_Z_010 m))

(cl:ensure-generic-function 'SARA_CF_Accel_X_010-val :lambda-list '(m))
(cl:defmethod SARA_CF_Accel_X_010-val ((m <SARA_06_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:SARA_CF_Accel_X_010-val is deprecated.  Use V2X_Integration-msg:SARA_CF_Accel_X_010 instead.")
  (SARA_CF_Accel_X_010 m))

(cl:ensure-generic-function 'SARA_CF_Accel_Y_010-val :lambda-list '(m))
(cl:defmethod SARA_CF_Accel_Y_010-val ((m <SARA_06_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:SARA_CF_Accel_Y_010-val is deprecated.  Use V2X_Integration-msg:SARA_CF_Accel_Y_010 instead.")
  (SARA_CF_Accel_Y_010 m))

(cl:ensure-generic-function 'SARA_CF_Omega_Z_010-val :lambda-list '(m))
(cl:defmethod SARA_CF_Omega_Z_010-val ((m <SARA_06_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:SARA_CF_Omega_Z_010-val is deprecated.  Use V2X_Integration-msg:SARA_CF_Omega_Z_010 instead.")
  (SARA_CF_Omega_Z_010 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SARA_06_Msg>) ostream)
  "Serializes a message object of type '<SARA_06_Msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'SARA_06_CRC)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'SARA_06_CRC)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'SARA_06_BZ)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'SARA_Accel_X_010))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'SARA_Accel_Y_010))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'SARA_Omega_Z_010))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'SARA_CF_Accel_X_010)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'SARA_CF_Accel_Y_010)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'SARA_CF_Omega_Z_010)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SARA_06_Msg>) istream)
  "Deserializes a message object of type '<SARA_06_Msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'SARA_06_CRC)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'SARA_06_CRC)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'SARA_06_BZ)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'SARA_Accel_X_010) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'SARA_Accel_Y_010) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'SARA_Omega_Z_010) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'SARA_CF_Accel_X_010)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'SARA_CF_Accel_Y_010)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'SARA_CF_Omega_Z_010)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SARA_06_Msg>)))
  "Returns string type for a message object of type '<SARA_06_Msg>"
  "V2X_Integration/SARA_06_Msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SARA_06_Msg)))
  "Returns string type for a message object of type 'SARA_06_Msg"
  "V2X_Integration/SARA_06_Msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SARA_06_Msg>)))
  "Returns md5sum for a message object of type '<SARA_06_Msg>"
  "2d6f91f1b10aaef29935d4bdfc80abae")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SARA_06_Msg)))
  "Returns md5sum for a message object of type 'SARA_06_Msg"
  "2d6f91f1b10aaef29935d4bdfc80abae")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SARA_06_Msg>)))
  "Returns full string definition for message of type '<SARA_06_Msg>"
  (cl:format cl:nil "Header header~%uint16 SARA_06_CRC~%uint8 SARA_06_BZ~%float32 SARA_Accel_X_010~%float32 SARA_Accel_Y_010~%float32 SARA_Omega_Z_010~%uint8 SARA_CF_Accel_X_010~%uint8 SARA_CF_Accel_Y_010~%uint8 SARA_CF_Omega_Z_010~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SARA_06_Msg)))
  "Returns full string definition for message of type 'SARA_06_Msg"
  (cl:format cl:nil "Header header~%uint16 SARA_06_CRC~%uint8 SARA_06_BZ~%float32 SARA_Accel_X_010~%float32 SARA_Accel_Y_010~%float32 SARA_Omega_Z_010~%uint8 SARA_CF_Accel_X_010~%uint8 SARA_CF_Accel_Y_010~%uint8 SARA_CF_Omega_Z_010~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SARA_06_Msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     2
     1
     4
     4
     4
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SARA_06_Msg>))
  "Converts a ROS message object to a list"
  (cl:list 'SARA_06_Msg
    (cl:cons ':header (header msg))
    (cl:cons ':SARA_06_CRC (SARA_06_CRC msg))
    (cl:cons ':SARA_06_BZ (SARA_06_BZ msg))
    (cl:cons ':SARA_Accel_X_010 (SARA_Accel_X_010 msg))
    (cl:cons ':SARA_Accel_Y_010 (SARA_Accel_Y_010 msg))
    (cl:cons ':SARA_Omega_Z_010 (SARA_Omega_Z_010 msg))
    (cl:cons ':SARA_CF_Accel_X_010 (SARA_CF_Accel_X_010 msg))
    (cl:cons ':SARA_CF_Accel_Y_010 (SARA_CF_Accel_Y_010 msg))
    (cl:cons ':SARA_CF_Omega_Z_010 (SARA_CF_Omega_Z_010 msg))
))
