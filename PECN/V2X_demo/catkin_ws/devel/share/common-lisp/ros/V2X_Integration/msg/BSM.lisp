; Auto-generated. Do not edit!


(cl:in-package V2X_Integration-msg)


;//! \htmlinclude BSM.msg.html

(cl:defclass <BSM> (roslisp-msg-protocol:ros-message)
  ((id
    :reader id
    :initarg :id
    :type cl:string
    :initform "")
   (sec_mark
    :reader sec_mark
    :initarg :sec_mark
    :type cl:float
    :initform 0.0)
   (message_count
    :reader message_count
    :initarg :message_count
    :type cl:fixnum
    :initform 0)
   (latitude
    :reader latitude
    :initarg :latitude
    :type cl:float
    :initform 0.0)
   (longtitude
    :reader longtitude
    :initarg :longtitude
    :type cl:float
    :initform 0.0)
   (elevation
    :reader elevation
    :initarg :elevation
    :type cl:float
    :initform 0.0)
   (pos_accuracy_semi_major
    :reader pos_accuracy_semi_major
    :initarg :pos_accuracy_semi_major
    :type cl:float
    :initform 0.0)
   (pos_accuracy_semi_minor
    :reader pos_accuracy_semi_minor
    :initarg :pos_accuracy_semi_minor
    :type cl:float
    :initform 0.0)
   (pos_accuracy_orientation
    :reader pos_accuracy_orientation
    :initarg :pos_accuracy_orientation
    :type cl:float
    :initform 0.0)
   (lateral_acceleration
    :reader lateral_acceleration
    :initarg :lateral_acceleration
    :type cl:float
    :initform 0.0)
   (longitudinal_acceleration
    :reader longitudinal_acceleration
    :initarg :longitudinal_acceleration
    :type cl:float
    :initform 0.0)
   (vert_acceleration
    :reader vert_acceleration
    :initarg :vert_acceleration
    :type cl:float
    :initform 0.0)
   (yaw_acceleration
    :reader yaw_acceleration
    :initarg :yaw_acceleration
    :type cl:float
    :initform 0.0)
   (transmission_state
    :reader transmission_state
    :initarg :transmission_state
    :type cl:fixnum
    :initform 0)
   (response_type
    :reader response_type
    :initarg :response_type
    :type cl:fixnum
    :initform 0)
   (light_use
    :reader light_use
    :initarg :light_use
    :type cl:fixnum
    :initform 0)
   (siren_use
    :reader siren_use
    :initarg :siren_use
    :type cl:fixnum
    :initform 0)
   (events
    :reader events
    :initarg :events
    :type cl:fixnum
    :initform 0)
   (lights
    :reader lights
    :initarg :lights
    :type cl:fixnum
    :initform 0)
   (confidence_position
    :reader confidence_position
    :initarg :confidence_position
    :type cl:fixnum
    :initform 0)
   (confidence_elevation
    :reader confidence_elevation
    :initarg :confidence_elevation
    :type cl:fixnum
    :initform 0)
   (vehicle_class
    :reader vehicle_class
    :initarg :vehicle_class
    :type cl:fixnum
    :initform 0)
   (vehicle_fuel_type
    :reader vehicle_fuel_type
    :initarg :vehicle_fuel_type
    :type cl:fixnum
    :initform 0)
   (heading
    :reader heading
    :initarg :heading
    :type cl:float
    :initform 0.0)
   (speed
    :reader speed
    :initarg :speed
    :type cl:float
    :initform 0.0)
   (angle
    :reader angle
    :initarg :angle
    :type cl:fixnum
    :initform 0)
   (vehicle_width
    :reader vehicle_width
    :initarg :vehicle_width
    :type cl:float
    :initform 0.0)
   (vehicle_lenth
    :reader vehicle_lenth
    :initarg :vehicle_lenth
    :type cl:float
    :initform 0.0)
   (vehicle_height
    :reader vehicle_height
    :initarg :vehicle_height
    :type cl:float
    :initform 0.0)
   (brake_padel
    :reader brake_padel
    :initarg :brake_padel
    :type cl:fixnum
    :initform 0)
   (wheel_brakes
    :reader wheel_brakes
    :initarg :wheel_brakes
    :type cl:fixnum
    :initform 0)
   (traction
    :reader traction
    :initarg :traction
    :type cl:fixnum
    :initform 0)
   (abs
    :reader abs
    :initarg :abs
    :type cl:fixnum
    :initform 0)
   (scs
    :reader scs
    :initarg :scs
    :type cl:fixnum
    :initform 0)
   (brake_boost
    :reader brake_boost
    :initarg :brake_boost
    :type cl:fixnum
    :initform 0)
   (aux_brakes
    :reader aux_brakes
    :initarg :aux_brakes
    :type cl:fixnum
    :initform 0))
)

(cl:defclass BSM (<BSM>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BSM>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BSM)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name V2X_Integration-msg:<BSM> is deprecated: use V2X_Integration-msg:BSM instead.")))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:id-val is deprecated.  Use V2X_Integration-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'sec_mark-val :lambda-list '(m))
(cl:defmethod sec_mark-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:sec_mark-val is deprecated.  Use V2X_Integration-msg:sec_mark instead.")
  (sec_mark m))

(cl:ensure-generic-function 'message_count-val :lambda-list '(m))
(cl:defmethod message_count-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:message_count-val is deprecated.  Use V2X_Integration-msg:message_count instead.")
  (message_count m))

(cl:ensure-generic-function 'latitude-val :lambda-list '(m))
(cl:defmethod latitude-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:latitude-val is deprecated.  Use V2X_Integration-msg:latitude instead.")
  (latitude m))

(cl:ensure-generic-function 'longtitude-val :lambda-list '(m))
(cl:defmethod longtitude-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:longtitude-val is deprecated.  Use V2X_Integration-msg:longtitude instead.")
  (longtitude m))

(cl:ensure-generic-function 'elevation-val :lambda-list '(m))
(cl:defmethod elevation-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:elevation-val is deprecated.  Use V2X_Integration-msg:elevation instead.")
  (elevation m))

(cl:ensure-generic-function 'pos_accuracy_semi_major-val :lambda-list '(m))
(cl:defmethod pos_accuracy_semi_major-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:pos_accuracy_semi_major-val is deprecated.  Use V2X_Integration-msg:pos_accuracy_semi_major instead.")
  (pos_accuracy_semi_major m))

(cl:ensure-generic-function 'pos_accuracy_semi_minor-val :lambda-list '(m))
(cl:defmethod pos_accuracy_semi_minor-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:pos_accuracy_semi_minor-val is deprecated.  Use V2X_Integration-msg:pos_accuracy_semi_minor instead.")
  (pos_accuracy_semi_minor m))

(cl:ensure-generic-function 'pos_accuracy_orientation-val :lambda-list '(m))
(cl:defmethod pos_accuracy_orientation-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:pos_accuracy_orientation-val is deprecated.  Use V2X_Integration-msg:pos_accuracy_orientation instead.")
  (pos_accuracy_orientation m))

(cl:ensure-generic-function 'lateral_acceleration-val :lambda-list '(m))
(cl:defmethod lateral_acceleration-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:lateral_acceleration-val is deprecated.  Use V2X_Integration-msg:lateral_acceleration instead.")
  (lateral_acceleration m))

(cl:ensure-generic-function 'longitudinal_acceleration-val :lambda-list '(m))
(cl:defmethod longitudinal_acceleration-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:longitudinal_acceleration-val is deprecated.  Use V2X_Integration-msg:longitudinal_acceleration instead.")
  (longitudinal_acceleration m))

(cl:ensure-generic-function 'vert_acceleration-val :lambda-list '(m))
(cl:defmethod vert_acceleration-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:vert_acceleration-val is deprecated.  Use V2X_Integration-msg:vert_acceleration instead.")
  (vert_acceleration m))

(cl:ensure-generic-function 'yaw_acceleration-val :lambda-list '(m))
(cl:defmethod yaw_acceleration-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:yaw_acceleration-val is deprecated.  Use V2X_Integration-msg:yaw_acceleration instead.")
  (yaw_acceleration m))

(cl:ensure-generic-function 'transmission_state-val :lambda-list '(m))
(cl:defmethod transmission_state-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:transmission_state-val is deprecated.  Use V2X_Integration-msg:transmission_state instead.")
  (transmission_state m))

(cl:ensure-generic-function 'response_type-val :lambda-list '(m))
(cl:defmethod response_type-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:response_type-val is deprecated.  Use V2X_Integration-msg:response_type instead.")
  (response_type m))

(cl:ensure-generic-function 'light_use-val :lambda-list '(m))
(cl:defmethod light_use-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:light_use-val is deprecated.  Use V2X_Integration-msg:light_use instead.")
  (light_use m))

(cl:ensure-generic-function 'siren_use-val :lambda-list '(m))
(cl:defmethod siren_use-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:siren_use-val is deprecated.  Use V2X_Integration-msg:siren_use instead.")
  (siren_use m))

(cl:ensure-generic-function 'events-val :lambda-list '(m))
(cl:defmethod events-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:events-val is deprecated.  Use V2X_Integration-msg:events instead.")
  (events m))

(cl:ensure-generic-function 'lights-val :lambda-list '(m))
(cl:defmethod lights-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:lights-val is deprecated.  Use V2X_Integration-msg:lights instead.")
  (lights m))

(cl:ensure-generic-function 'confidence_position-val :lambda-list '(m))
(cl:defmethod confidence_position-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:confidence_position-val is deprecated.  Use V2X_Integration-msg:confidence_position instead.")
  (confidence_position m))

(cl:ensure-generic-function 'confidence_elevation-val :lambda-list '(m))
(cl:defmethod confidence_elevation-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:confidence_elevation-val is deprecated.  Use V2X_Integration-msg:confidence_elevation instead.")
  (confidence_elevation m))

(cl:ensure-generic-function 'vehicle_class-val :lambda-list '(m))
(cl:defmethod vehicle_class-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:vehicle_class-val is deprecated.  Use V2X_Integration-msg:vehicle_class instead.")
  (vehicle_class m))

(cl:ensure-generic-function 'vehicle_fuel_type-val :lambda-list '(m))
(cl:defmethod vehicle_fuel_type-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:vehicle_fuel_type-val is deprecated.  Use V2X_Integration-msg:vehicle_fuel_type instead.")
  (vehicle_fuel_type m))

(cl:ensure-generic-function 'heading-val :lambda-list '(m))
(cl:defmethod heading-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:heading-val is deprecated.  Use V2X_Integration-msg:heading instead.")
  (heading m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:speed-val is deprecated.  Use V2X_Integration-msg:speed instead.")
  (speed m))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:angle-val is deprecated.  Use V2X_Integration-msg:angle instead.")
  (angle m))

(cl:ensure-generic-function 'vehicle_width-val :lambda-list '(m))
(cl:defmethod vehicle_width-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:vehicle_width-val is deprecated.  Use V2X_Integration-msg:vehicle_width instead.")
  (vehicle_width m))

(cl:ensure-generic-function 'vehicle_lenth-val :lambda-list '(m))
(cl:defmethod vehicle_lenth-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:vehicle_lenth-val is deprecated.  Use V2X_Integration-msg:vehicle_lenth instead.")
  (vehicle_lenth m))

(cl:ensure-generic-function 'vehicle_height-val :lambda-list '(m))
(cl:defmethod vehicle_height-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:vehicle_height-val is deprecated.  Use V2X_Integration-msg:vehicle_height instead.")
  (vehicle_height m))

(cl:ensure-generic-function 'brake_padel-val :lambda-list '(m))
(cl:defmethod brake_padel-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:brake_padel-val is deprecated.  Use V2X_Integration-msg:brake_padel instead.")
  (brake_padel m))

(cl:ensure-generic-function 'wheel_brakes-val :lambda-list '(m))
(cl:defmethod wheel_brakes-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:wheel_brakes-val is deprecated.  Use V2X_Integration-msg:wheel_brakes instead.")
  (wheel_brakes m))

(cl:ensure-generic-function 'traction-val :lambda-list '(m))
(cl:defmethod traction-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:traction-val is deprecated.  Use V2X_Integration-msg:traction instead.")
  (traction m))

(cl:ensure-generic-function 'abs-val :lambda-list '(m))
(cl:defmethod abs-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:abs-val is deprecated.  Use V2X_Integration-msg:abs instead.")
  (abs m))

(cl:ensure-generic-function 'scs-val :lambda-list '(m))
(cl:defmethod scs-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:scs-val is deprecated.  Use V2X_Integration-msg:scs instead.")
  (scs m))

(cl:ensure-generic-function 'brake_boost-val :lambda-list '(m))
(cl:defmethod brake_boost-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:brake_boost-val is deprecated.  Use V2X_Integration-msg:brake_boost instead.")
  (brake_boost m))

(cl:ensure-generic-function 'aux_brakes-val :lambda-list '(m))
(cl:defmethod aux_brakes-val ((m <BSM>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:aux_brakes-val is deprecated.  Use V2X_Integration-msg:aux_brakes instead.")
  (aux_brakes m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BSM>) ostream)
  "Serializes a message object of type '<BSM>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'id))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'id))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'sec_mark))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'message_count)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'latitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'longtitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'elevation))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pos_accuracy_semi_major))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pos_accuracy_semi_minor))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pos_accuracy_orientation))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'lateral_acceleration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'longitudinal_acceleration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'vert_acceleration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'yaw_acceleration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'transmission_state)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'response_type)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'light_use)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'siren_use)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'events)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'lights)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'confidence_position)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'confidence_elevation)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'vehicle_class)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'vehicle_fuel_type)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'heading))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'angle)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'vehicle_width))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'vehicle_lenth))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'vehicle_height))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'brake_padel)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'wheel_brakes)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'traction)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'abs)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'scs)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'brake_boost)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'aux_brakes)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BSM>) istream)
  "Deserializes a message object of type '<BSM>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'id) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'id) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'sec_mark) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'message_count) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'latitude) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'longtitude) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'elevation) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pos_accuracy_semi_major) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pos_accuracy_semi_minor) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pos_accuracy_orientation) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'lateral_acceleration) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'longitudinal_acceleration) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'vert_acceleration) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'yaw_acceleration) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'transmission_state)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'response_type)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'light_use)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'siren_use)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'events)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'lights)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'confidence_position)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'confidence_elevation)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'vehicle_class)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'vehicle_fuel_type)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'heading) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'speed) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'angle) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'vehicle_width) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'vehicle_lenth) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'vehicle_height) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'brake_padel)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'wheel_brakes)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'traction)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'abs)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'scs)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'brake_boost)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'aux_brakes)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BSM>)))
  "Returns string type for a message object of type '<BSM>"
  "V2X_Integration/BSM")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BSM)))
  "Returns string type for a message object of type 'BSM"
  "V2X_Integration/BSM")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BSM>)))
  "Returns md5sum for a message object of type '<BSM>"
  "e6940b8bdce7382d047211cc39f10e12")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BSM)))
  "Returns md5sum for a message object of type 'BSM"
  "e6940b8bdce7382d047211cc39f10e12")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BSM>)))
  "Returns full string definition for message of type '<BSM>"
  (cl:format cl:nil "string id~%float32 sec_mark~%int16 message_count~%float32 latitude~%float32 longtitude~%float32 elevation~%float32 pos_accuracy_semi_major~%float32 pos_accuracy_semi_minor~%float32 pos_accuracy_orientation~%float32 lateral_acceleration~%float32 longitudinal_acceleration~%float32 vert_acceleration~%float32 yaw_acceleration~%uint8 transmission_state~%uint8 response_type~%uint8 light_use~%uint8 siren_use~%uint8 events~%uint8 lights~%uint8 confidence_position~%uint8 confidence_elevation~%uint8 vehicle_class~%uint8 vehicle_fuel_type~%float32 heading~%float32 speed~%int16 angle~%float32 vehicle_width~%float32 vehicle_lenth~%float32 vehicle_height~%uint8 brake_padel~%uint8 wheel_brakes~%uint8 traction~%uint8 abs~%uint8 scs~%uint8 brake_boost~%uint8 aux_brakes~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BSM)))
  "Returns full string definition for message of type 'BSM"
  (cl:format cl:nil "string id~%float32 sec_mark~%int16 message_count~%float32 latitude~%float32 longtitude~%float32 elevation~%float32 pos_accuracy_semi_major~%float32 pos_accuracy_semi_minor~%float32 pos_accuracy_orientation~%float32 lateral_acceleration~%float32 longitudinal_acceleration~%float32 vert_acceleration~%float32 yaw_acceleration~%uint8 transmission_state~%uint8 response_type~%uint8 light_use~%uint8 siren_use~%uint8 events~%uint8 lights~%uint8 confidence_position~%uint8 confidence_elevation~%uint8 vehicle_class~%uint8 vehicle_fuel_type~%float32 heading~%float32 speed~%int16 angle~%float32 vehicle_width~%float32 vehicle_lenth~%float32 vehicle_height~%uint8 brake_padel~%uint8 wheel_brakes~%uint8 traction~%uint8 abs~%uint8 scs~%uint8 brake_boost~%uint8 aux_brakes~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BSM>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'id))
     4
     2
     4
     4
     4
     4
     4
     4
     4
     4
     4
     4
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     4
     4
     2
     4
     4
     4
     1
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BSM>))
  "Converts a ROS message object to a list"
  (cl:list 'BSM
    (cl:cons ':id (id msg))
    (cl:cons ':sec_mark (sec_mark msg))
    (cl:cons ':message_count (message_count msg))
    (cl:cons ':latitude (latitude msg))
    (cl:cons ':longtitude (longtitude msg))
    (cl:cons ':elevation (elevation msg))
    (cl:cons ':pos_accuracy_semi_major (pos_accuracy_semi_major msg))
    (cl:cons ':pos_accuracy_semi_minor (pos_accuracy_semi_minor msg))
    (cl:cons ':pos_accuracy_orientation (pos_accuracy_orientation msg))
    (cl:cons ':lateral_acceleration (lateral_acceleration msg))
    (cl:cons ':longitudinal_acceleration (longitudinal_acceleration msg))
    (cl:cons ':vert_acceleration (vert_acceleration msg))
    (cl:cons ':yaw_acceleration (yaw_acceleration msg))
    (cl:cons ':transmission_state (transmission_state msg))
    (cl:cons ':response_type (response_type msg))
    (cl:cons ':light_use (light_use msg))
    (cl:cons ':siren_use (siren_use msg))
    (cl:cons ':events (events msg))
    (cl:cons ':lights (lights msg))
    (cl:cons ':confidence_position (confidence_position msg))
    (cl:cons ':confidence_elevation (confidence_elevation msg))
    (cl:cons ':vehicle_class (vehicle_class msg))
    (cl:cons ':vehicle_fuel_type (vehicle_fuel_type msg))
    (cl:cons ':heading (heading msg))
    (cl:cons ':speed (speed msg))
    (cl:cons ':angle (angle msg))
    (cl:cons ':vehicle_width (vehicle_width msg))
    (cl:cons ':vehicle_lenth (vehicle_lenth msg))
    (cl:cons ':vehicle_height (vehicle_height msg))
    (cl:cons ':brake_padel (brake_padel msg))
    (cl:cons ':wheel_brakes (wheel_brakes msg))
    (cl:cons ':traction (traction msg))
    (cl:cons ':abs (abs msg))
    (cl:cons ':scs (scs msg))
    (cl:cons ':brake_boost (brake_boost msg))
    (cl:cons ':aux_brakes (aux_brakes msg))
))
