; Auto-generated. Do not edit!


(cl:in-package V2X_Integration-msg)


;//! \htmlinclude FB_05_Msg.msg.html

(cl:defclass <FB_05_Msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (FB_Kopfrotation_Gier_Guete
    :reader FB_Kopfrotation_Gier_Guete
    :initarg :FB_Kopfrotation_Gier_Guete
    :type cl:float
    :initform 0.0)
   (FB_Kopfposition_Z_Guete
    :reader FB_Kopfposition_Z_Guete
    :initarg :FB_Kopfposition_Z_Guete
    :type cl:float
    :initform 0.0)
   (FB_Kopfposition_Y_Guete
    :reader FB_Kopfposition_Y_Guete
    :initarg :FB_Kopfposition_Y_Guete
    :type cl:float
    :initform 0.0)
   (FB_Kopfposition_X_Guete
    :reader FB_Kopfposition_X_Guete
    :initarg :FB_Kopfposition_X_Guete
    :type cl:float
    :initform 0.0)
   (FB_Kopfrotation_Gier
    :reader FB_Kopfrotation_Gier
    :initarg :FB_Kopfrotation_Gier
    :type cl:float
    :initform 0.0)
   (FB_Kopfposition_Z
    :reader FB_Kopfposition_Z
    :initarg :FB_Kopfposition_Z
    :type cl:float
    :initform 0.0)
   (FB_Kopfposition_Y
    :reader FB_Kopfposition_Y
    :initarg :FB_Kopfposition_Y
    :type cl:float
    :initform 0.0)
   (FB_Kopfposition_X
    :reader FB_Kopfposition_X
    :initarg :FB_Kopfposition_X
    :type cl:float
    :initform 0.0))
)

(cl:defclass FB_05_Msg (<FB_05_Msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FB_05_Msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FB_05_Msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name V2X_Integration-msg:<FB_05_Msg> is deprecated: use V2X_Integration-msg:FB_05_Msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <FB_05_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:header-val is deprecated.  Use V2X_Integration-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'FB_Kopfrotation_Gier_Guete-val :lambda-list '(m))
(cl:defmethod FB_Kopfrotation_Gier_Guete-val ((m <FB_05_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:FB_Kopfrotation_Gier_Guete-val is deprecated.  Use V2X_Integration-msg:FB_Kopfrotation_Gier_Guete instead.")
  (FB_Kopfrotation_Gier_Guete m))

(cl:ensure-generic-function 'FB_Kopfposition_Z_Guete-val :lambda-list '(m))
(cl:defmethod FB_Kopfposition_Z_Guete-val ((m <FB_05_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:FB_Kopfposition_Z_Guete-val is deprecated.  Use V2X_Integration-msg:FB_Kopfposition_Z_Guete instead.")
  (FB_Kopfposition_Z_Guete m))

(cl:ensure-generic-function 'FB_Kopfposition_Y_Guete-val :lambda-list '(m))
(cl:defmethod FB_Kopfposition_Y_Guete-val ((m <FB_05_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:FB_Kopfposition_Y_Guete-val is deprecated.  Use V2X_Integration-msg:FB_Kopfposition_Y_Guete instead.")
  (FB_Kopfposition_Y_Guete m))

(cl:ensure-generic-function 'FB_Kopfposition_X_Guete-val :lambda-list '(m))
(cl:defmethod FB_Kopfposition_X_Guete-val ((m <FB_05_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:FB_Kopfposition_X_Guete-val is deprecated.  Use V2X_Integration-msg:FB_Kopfposition_X_Guete instead.")
  (FB_Kopfposition_X_Guete m))

(cl:ensure-generic-function 'FB_Kopfrotation_Gier-val :lambda-list '(m))
(cl:defmethod FB_Kopfrotation_Gier-val ((m <FB_05_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:FB_Kopfrotation_Gier-val is deprecated.  Use V2X_Integration-msg:FB_Kopfrotation_Gier instead.")
  (FB_Kopfrotation_Gier m))

(cl:ensure-generic-function 'FB_Kopfposition_Z-val :lambda-list '(m))
(cl:defmethod FB_Kopfposition_Z-val ((m <FB_05_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:FB_Kopfposition_Z-val is deprecated.  Use V2X_Integration-msg:FB_Kopfposition_Z instead.")
  (FB_Kopfposition_Z m))

(cl:ensure-generic-function 'FB_Kopfposition_Y-val :lambda-list '(m))
(cl:defmethod FB_Kopfposition_Y-val ((m <FB_05_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:FB_Kopfposition_Y-val is deprecated.  Use V2X_Integration-msg:FB_Kopfposition_Y instead.")
  (FB_Kopfposition_Y m))

(cl:ensure-generic-function 'FB_Kopfposition_X-val :lambda-list '(m))
(cl:defmethod FB_Kopfposition_X-val ((m <FB_05_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:FB_Kopfposition_X-val is deprecated.  Use V2X_Integration-msg:FB_Kopfposition_X instead.")
  (FB_Kopfposition_X m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FB_05_Msg>) ostream)
  "Serializes a message object of type '<FB_05_Msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'FB_Kopfrotation_Gier_Guete))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'FB_Kopfposition_Z_Guete))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'FB_Kopfposition_Y_Guete))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'FB_Kopfposition_X_Guete))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'FB_Kopfrotation_Gier))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'FB_Kopfposition_Z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'FB_Kopfposition_Y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'FB_Kopfposition_X))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FB_05_Msg>) istream)
  "Deserializes a message object of type '<FB_05_Msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'FB_Kopfrotation_Gier_Guete) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'FB_Kopfposition_Z_Guete) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'FB_Kopfposition_Y_Guete) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'FB_Kopfposition_X_Guete) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'FB_Kopfrotation_Gier) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'FB_Kopfposition_Z) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'FB_Kopfposition_Y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'FB_Kopfposition_X) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FB_05_Msg>)))
  "Returns string type for a message object of type '<FB_05_Msg>"
  "V2X_Integration/FB_05_Msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FB_05_Msg)))
  "Returns string type for a message object of type 'FB_05_Msg"
  "V2X_Integration/FB_05_Msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FB_05_Msg>)))
  "Returns md5sum for a message object of type '<FB_05_Msg>"
  "e0505810bf77d4eb9eb73dfc0b88136b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FB_05_Msg)))
  "Returns md5sum for a message object of type 'FB_05_Msg"
  "e0505810bf77d4eb9eb73dfc0b88136b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FB_05_Msg>)))
  "Returns full string definition for message of type '<FB_05_Msg>"
  (cl:format cl:nil "Header header~%float32 FB_Kopfrotation_Gier_Guete~%float32 FB_Kopfposition_Z_Guete~%float32 FB_Kopfposition_Y_Guete~%float32 FB_Kopfposition_X_Guete~%float32 FB_Kopfrotation_Gier~%float32 FB_Kopfposition_Z~%float32 FB_Kopfposition_Y~%float32 FB_Kopfposition_X~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FB_05_Msg)))
  "Returns full string definition for message of type 'FB_05_Msg"
  (cl:format cl:nil "Header header~%float32 FB_Kopfrotation_Gier_Guete~%float32 FB_Kopfposition_Z_Guete~%float32 FB_Kopfposition_Y_Guete~%float32 FB_Kopfposition_X_Guete~%float32 FB_Kopfrotation_Gier~%float32 FB_Kopfposition_Z~%float32 FB_Kopfposition_Y~%float32 FB_Kopfposition_X~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FB_05_Msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FB_05_Msg>))
  "Converts a ROS message object to a list"
  (cl:list 'FB_05_Msg
    (cl:cons ':header (header msg))
    (cl:cons ':FB_Kopfrotation_Gier_Guete (FB_Kopfrotation_Gier_Guete msg))
    (cl:cons ':FB_Kopfposition_Z_Guete (FB_Kopfposition_Z_Guete msg))
    (cl:cons ':FB_Kopfposition_Y_Guete (FB_Kopfposition_Y_Guete msg))
    (cl:cons ':FB_Kopfposition_X_Guete (FB_Kopfposition_X_Guete msg))
    (cl:cons ':FB_Kopfrotation_Gier (FB_Kopfrotation_Gier msg))
    (cl:cons ':FB_Kopfposition_Z (FB_Kopfposition_Z msg))
    (cl:cons ':FB_Kopfposition_Y (FB_Kopfposition_Y msg))
    (cl:cons ':FB_Kopfposition_X (FB_Kopfposition_X msg))
))
