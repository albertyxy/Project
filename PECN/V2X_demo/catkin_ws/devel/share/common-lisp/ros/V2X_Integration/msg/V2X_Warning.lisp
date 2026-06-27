; Auto-generated. Do not edit!


(cl:in-package V2X_Integration-msg)


;//! \htmlinclude V2X_Warning.msg.html

(cl:defclass <V2X_Warning> (roslisp-msg-protocol:ros-message)
  ((warning_level
    :reader warning_level
    :initarg :warning_level
    :type cl:fixnum
    :initform 0))
)

(cl:defclass V2X_Warning (<V2X_Warning>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <V2X_Warning>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'V2X_Warning)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name V2X_Integration-msg:<V2X_Warning> is deprecated: use V2X_Integration-msg:V2X_Warning instead.")))

(cl:ensure-generic-function 'warning_level-val :lambda-list '(m))
(cl:defmethod warning_level-val ((m <V2X_Warning>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:warning_level-val is deprecated.  Use V2X_Integration-msg:warning_level instead.")
  (warning_level m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <V2X_Warning>) ostream)
  "Serializes a message object of type '<V2X_Warning>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'warning_level)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <V2X_Warning>) istream)
  "Deserializes a message object of type '<V2X_Warning>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'warning_level)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<V2X_Warning>)))
  "Returns string type for a message object of type '<V2X_Warning>"
  "V2X_Integration/V2X_Warning")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'V2X_Warning)))
  "Returns string type for a message object of type 'V2X_Warning"
  "V2X_Integration/V2X_Warning")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<V2X_Warning>)))
  "Returns md5sum for a message object of type '<V2X_Warning>"
  "140cc051af28c9742e4f2dcebd133a9b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'V2X_Warning)))
  "Returns md5sum for a message object of type 'V2X_Warning"
  "140cc051af28c9742e4f2dcebd133a9b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<V2X_Warning>)))
  "Returns full string definition for message of type '<V2X_Warning>"
  (cl:format cl:nil "uint8 warning_level~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'V2X_Warning)))
  "Returns full string definition for message of type 'V2X_Warning"
  (cl:format cl:nil "uint8 warning_level~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <V2X_Warning>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <V2X_Warning>))
  "Converts a ROS message object to a list"
  (cl:list 'V2X_Warning
    (cl:cons ':warning_level (warning_level msg))
))
