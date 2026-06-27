; Auto-generated. Do not edit!


(cl:in-package V2X_Integration-msg)


;//! \htmlinclude ESP_21_Msg.msg.html

(cl:defclass <ESP_21_Msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (ESP_21_CRC
    :reader ESP_21_CRC
    :initarg :ESP_21_CRC
    :type cl:fixnum
    :initform 0)
   (ESP_21_BZ
    :reader ESP_21_BZ
    :initarg :ESP_21_BZ
    :type cl:fixnum
    :initform 0)
   (BR_Eingriffsmoment
    :reader BR_Eingriffsmoment
    :initarg :BR_Eingriffsmoment
    :type cl:fixnum
    :initform 0)
   (ESP_Diagnose
    :reader ESP_Diagnose
    :initarg :ESP_Diagnose
    :type cl:fixnum
    :initform 0)
   (ESC_v_Signal_Qualifier_High_Low
    :reader ESC_v_Signal_Qualifier_High_Low
    :initarg :ESC_v_Signal_Qualifier_High_Low
    :type cl:fixnum
    :initform 0)
   (ESP_Vorsteuerung
    :reader ESP_Vorsteuerung
    :initarg :ESP_Vorsteuerung
    :type cl:fixnum
    :initform 0)
   (OBD_Schlechtweg
    :reader OBD_Schlechtweg
    :initarg :OBD_Schlechtweg
    :type cl:fixnum
    :initform 0)
   (OBD_QBit_Schlechtweg
    :reader OBD_QBit_Schlechtweg
    :initarg :OBD_QBit_Schlechtweg
    :type cl:fixnum
    :initform 0)
   (ESP_v_Signal
    :reader ESP_v_Signal
    :initarg :ESP_v_Signal
    :type cl:float
    :initform 0.0)
   (ASR_Tastung_passiv
    :reader ASR_Tastung_passiv
    :initarg :ASR_Tastung_passiv
    :type cl:fixnum
    :initform 0)
   (ESP_Tastung_passiv
    :reader ESP_Tastung_passiv
    :initarg :ESP_Tastung_passiv
    :type cl:fixnum
    :initform 0)
   (ESP_Systemstatus
    :reader ESP_Systemstatus
    :initarg :ESP_Systemstatus
    :type cl:fixnum
    :initform 0)
   (ASR_Schalteingriff
    :reader ASR_Schalteingriff
    :initarg :ASR_Schalteingriff
    :type cl:fixnum
    :initform 0)
   (ESP_QBit_v_Signal
    :reader ESP_QBit_v_Signal
    :initarg :ESP_QBit_v_Signal
    :type cl:fixnum
    :initform 0)
   (ABS_Bremsung
    :reader ABS_Bremsung
    :initarg :ABS_Bremsung
    :type cl:fixnum
    :initform 0)
   (ASR_Anf
    :reader ASR_Anf
    :initarg :ASR_Anf
    :type cl:fixnum
    :initform 0)
   (MSR_Anf
    :reader MSR_Anf
    :initarg :MSR_Anf
    :type cl:fixnum
    :initform 0)
   (EBV_Eingriff
    :reader EBV_Eingriff
    :initarg :EBV_Eingriff
    :type cl:fixnum
    :initform 0)
   (EDS_Eingriff
    :reader EDS_Eingriff
    :initarg :EDS_Eingriff
    :type cl:fixnum
    :initform 0)
   (ESP_Eingriff
    :reader ESP_Eingriff
    :initarg :ESP_Eingriff
    :type cl:fixnum
    :initform 0)
   (ESP_ASP
    :reader ESP_ASP
    :initarg :ESP_ASP
    :type cl:fixnum
    :initform 0)
   (ESC_Neutralschaltung
    :reader ESC_Neutralschaltung
    :initarg :ESC_Neutralschaltung
    :type cl:fixnum
    :initform 0))
)

(cl:defclass ESP_21_Msg (<ESP_21_Msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ESP_21_Msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ESP_21_Msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name V2X_Integration-msg:<ESP_21_Msg> is deprecated: use V2X_Integration-msg:ESP_21_Msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:header-val is deprecated.  Use V2X_Integration-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'ESP_21_CRC-val :lambda-list '(m))
(cl:defmethod ESP_21_CRC-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ESP_21_CRC-val is deprecated.  Use V2X_Integration-msg:ESP_21_CRC instead.")
  (ESP_21_CRC m))

(cl:ensure-generic-function 'ESP_21_BZ-val :lambda-list '(m))
(cl:defmethod ESP_21_BZ-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ESP_21_BZ-val is deprecated.  Use V2X_Integration-msg:ESP_21_BZ instead.")
  (ESP_21_BZ m))

(cl:ensure-generic-function 'BR_Eingriffsmoment-val :lambda-list '(m))
(cl:defmethod BR_Eingriffsmoment-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:BR_Eingriffsmoment-val is deprecated.  Use V2X_Integration-msg:BR_Eingriffsmoment instead.")
  (BR_Eingriffsmoment m))

(cl:ensure-generic-function 'ESP_Diagnose-val :lambda-list '(m))
(cl:defmethod ESP_Diagnose-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ESP_Diagnose-val is deprecated.  Use V2X_Integration-msg:ESP_Diagnose instead.")
  (ESP_Diagnose m))

(cl:ensure-generic-function 'ESC_v_Signal_Qualifier_High_Low-val :lambda-list '(m))
(cl:defmethod ESC_v_Signal_Qualifier_High_Low-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ESC_v_Signal_Qualifier_High_Low-val is deprecated.  Use V2X_Integration-msg:ESC_v_Signal_Qualifier_High_Low instead.")
  (ESC_v_Signal_Qualifier_High_Low m))

(cl:ensure-generic-function 'ESP_Vorsteuerung-val :lambda-list '(m))
(cl:defmethod ESP_Vorsteuerung-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ESP_Vorsteuerung-val is deprecated.  Use V2X_Integration-msg:ESP_Vorsteuerung instead.")
  (ESP_Vorsteuerung m))

(cl:ensure-generic-function 'OBD_Schlechtweg-val :lambda-list '(m))
(cl:defmethod OBD_Schlechtweg-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:OBD_Schlechtweg-val is deprecated.  Use V2X_Integration-msg:OBD_Schlechtweg instead.")
  (OBD_Schlechtweg m))

(cl:ensure-generic-function 'OBD_QBit_Schlechtweg-val :lambda-list '(m))
(cl:defmethod OBD_QBit_Schlechtweg-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:OBD_QBit_Schlechtweg-val is deprecated.  Use V2X_Integration-msg:OBD_QBit_Schlechtweg instead.")
  (OBD_QBit_Schlechtweg m))

(cl:ensure-generic-function 'ESP_v_Signal-val :lambda-list '(m))
(cl:defmethod ESP_v_Signal-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ESP_v_Signal-val is deprecated.  Use V2X_Integration-msg:ESP_v_Signal instead.")
  (ESP_v_Signal m))

(cl:ensure-generic-function 'ASR_Tastung_passiv-val :lambda-list '(m))
(cl:defmethod ASR_Tastung_passiv-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ASR_Tastung_passiv-val is deprecated.  Use V2X_Integration-msg:ASR_Tastung_passiv instead.")
  (ASR_Tastung_passiv m))

(cl:ensure-generic-function 'ESP_Tastung_passiv-val :lambda-list '(m))
(cl:defmethod ESP_Tastung_passiv-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ESP_Tastung_passiv-val is deprecated.  Use V2X_Integration-msg:ESP_Tastung_passiv instead.")
  (ESP_Tastung_passiv m))

(cl:ensure-generic-function 'ESP_Systemstatus-val :lambda-list '(m))
(cl:defmethod ESP_Systemstatus-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ESP_Systemstatus-val is deprecated.  Use V2X_Integration-msg:ESP_Systemstatus instead.")
  (ESP_Systemstatus m))

(cl:ensure-generic-function 'ASR_Schalteingriff-val :lambda-list '(m))
(cl:defmethod ASR_Schalteingriff-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ASR_Schalteingriff-val is deprecated.  Use V2X_Integration-msg:ASR_Schalteingriff instead.")
  (ASR_Schalteingriff m))

(cl:ensure-generic-function 'ESP_QBit_v_Signal-val :lambda-list '(m))
(cl:defmethod ESP_QBit_v_Signal-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ESP_QBit_v_Signal-val is deprecated.  Use V2X_Integration-msg:ESP_QBit_v_Signal instead.")
  (ESP_QBit_v_Signal m))

(cl:ensure-generic-function 'ABS_Bremsung-val :lambda-list '(m))
(cl:defmethod ABS_Bremsung-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ABS_Bremsung-val is deprecated.  Use V2X_Integration-msg:ABS_Bremsung instead.")
  (ABS_Bremsung m))

(cl:ensure-generic-function 'ASR_Anf-val :lambda-list '(m))
(cl:defmethod ASR_Anf-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ASR_Anf-val is deprecated.  Use V2X_Integration-msg:ASR_Anf instead.")
  (ASR_Anf m))

(cl:ensure-generic-function 'MSR_Anf-val :lambda-list '(m))
(cl:defmethod MSR_Anf-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:MSR_Anf-val is deprecated.  Use V2X_Integration-msg:MSR_Anf instead.")
  (MSR_Anf m))

(cl:ensure-generic-function 'EBV_Eingriff-val :lambda-list '(m))
(cl:defmethod EBV_Eingriff-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:EBV_Eingriff-val is deprecated.  Use V2X_Integration-msg:EBV_Eingriff instead.")
  (EBV_Eingriff m))

(cl:ensure-generic-function 'EDS_Eingriff-val :lambda-list '(m))
(cl:defmethod EDS_Eingriff-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:EDS_Eingriff-val is deprecated.  Use V2X_Integration-msg:EDS_Eingriff instead.")
  (EDS_Eingriff m))

(cl:ensure-generic-function 'ESP_Eingriff-val :lambda-list '(m))
(cl:defmethod ESP_Eingriff-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ESP_Eingriff-val is deprecated.  Use V2X_Integration-msg:ESP_Eingriff instead.")
  (ESP_Eingriff m))

(cl:ensure-generic-function 'ESP_ASP-val :lambda-list '(m))
(cl:defmethod ESP_ASP-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ESP_ASP-val is deprecated.  Use V2X_Integration-msg:ESP_ASP instead.")
  (ESP_ASP m))

(cl:ensure-generic-function 'ESC_Neutralschaltung-val :lambda-list '(m))
(cl:defmethod ESC_Neutralschaltung-val ((m <ESP_21_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader V2X_Integration-msg:ESC_Neutralschaltung-val is deprecated.  Use V2X_Integration-msg:ESC_Neutralschaltung instead.")
  (ESC_Neutralschaltung m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ESP_21_Msg>) ostream)
  "Serializes a message object of type '<ESP_21_Msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_21_CRC)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'ESP_21_CRC)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_21_BZ)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'BR_Eingriffsmoment)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_Diagnose)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESC_v_Signal_Qualifier_High_Low)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_Vorsteuerung)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'OBD_Schlechtweg)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'OBD_QBit_Schlechtweg)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'ESP_v_Signal))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ASR_Tastung_passiv)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_Tastung_passiv)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_Systemstatus)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ASR_Schalteingriff)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_QBit_v_Signal)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ABS_Bremsung)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ASR_Anf)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'MSR_Anf)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'EBV_Eingriff)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'EDS_Eingriff)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_Eingriff)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_ASP)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESC_Neutralschaltung)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ESP_21_Msg>) istream)
  "Deserializes a message object of type '<ESP_21_Msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_21_CRC)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'ESP_21_CRC)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_21_BZ)) (cl:read-byte istream))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'BR_Eingriffsmoment) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_Diagnose)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESC_v_Signal_Qualifier_High_Low)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_Vorsteuerung)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'OBD_Schlechtweg)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'OBD_QBit_Schlechtweg)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'ESP_v_Signal) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ASR_Tastung_passiv)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_Tastung_passiv)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_Systemstatus)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ASR_Schalteingriff)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_QBit_v_Signal)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ABS_Bremsung)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ASR_Anf)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'MSR_Anf)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'EBV_Eingriff)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'EDS_Eingriff)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_Eingriff)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESP_ASP)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ESC_Neutralschaltung)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ESP_21_Msg>)))
  "Returns string type for a message object of type '<ESP_21_Msg>"
  "V2X_Integration/ESP_21_Msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ESP_21_Msg)))
  "Returns string type for a message object of type 'ESP_21_Msg"
  "V2X_Integration/ESP_21_Msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ESP_21_Msg>)))
  "Returns md5sum for a message object of type '<ESP_21_Msg>"
  "14034e15be32d792bb36bad51c5aaa1b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ESP_21_Msg)))
  "Returns md5sum for a message object of type 'ESP_21_Msg"
  "14034e15be32d792bb36bad51c5aaa1b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ESP_21_Msg>)))
  "Returns full string definition for message of type '<ESP_21_Msg>"
  (cl:format cl:nil "Header header~%uint16 ESP_21_CRC~%uint8 ESP_21_BZ~%int16 BR_Eingriffsmoment~%uint8 ESP_Diagnose~%uint8 ESC_v_Signal_Qualifier_High_Low~%uint8 ESP_Vorsteuerung~%uint8 OBD_Schlechtweg~%uint8 OBD_QBit_Schlechtweg~%float32 ESP_v_Signal~%uint8 ASR_Tastung_passiv~%uint8 ESP_Tastung_passiv~%uint8 ESP_Systemstatus~%uint8 ASR_Schalteingriff~%uint8 ESP_QBit_v_Signal~%uint8 ABS_Bremsung~%uint8 ASR_Anf~%uint8 MSR_Anf~%uint8 EBV_Eingriff~%uint8 EDS_Eingriff~%uint8 ESP_Eingriff~%uint8 ESP_ASP~%uint8 ESC_Neutralschaltung~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ESP_21_Msg)))
  "Returns full string definition for message of type 'ESP_21_Msg"
  (cl:format cl:nil "Header header~%uint16 ESP_21_CRC~%uint8 ESP_21_BZ~%int16 BR_Eingriffsmoment~%uint8 ESP_Diagnose~%uint8 ESC_v_Signal_Qualifier_High_Low~%uint8 ESP_Vorsteuerung~%uint8 OBD_Schlechtweg~%uint8 OBD_QBit_Schlechtweg~%float32 ESP_v_Signal~%uint8 ASR_Tastung_passiv~%uint8 ESP_Tastung_passiv~%uint8 ESP_Systemstatus~%uint8 ASR_Schalteingriff~%uint8 ESP_QBit_v_Signal~%uint8 ABS_Bremsung~%uint8 ASR_Anf~%uint8 MSR_Anf~%uint8 EBV_Eingriff~%uint8 EDS_Eingriff~%uint8 ESP_Eingriff~%uint8 ESP_ASP~%uint8 ESC_Neutralschaltung~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ESP_21_Msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     2
     1
     2
     1
     1
     1
     1
     1
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
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ESP_21_Msg>))
  "Converts a ROS message object to a list"
  (cl:list 'ESP_21_Msg
    (cl:cons ':header (header msg))
    (cl:cons ':ESP_21_CRC (ESP_21_CRC msg))
    (cl:cons ':ESP_21_BZ (ESP_21_BZ msg))
    (cl:cons ':BR_Eingriffsmoment (BR_Eingriffsmoment msg))
    (cl:cons ':ESP_Diagnose (ESP_Diagnose msg))
    (cl:cons ':ESC_v_Signal_Qualifier_High_Low (ESC_v_Signal_Qualifier_High_Low msg))
    (cl:cons ':ESP_Vorsteuerung (ESP_Vorsteuerung msg))
    (cl:cons ':OBD_Schlechtweg (OBD_Schlechtweg msg))
    (cl:cons ':OBD_QBit_Schlechtweg (OBD_QBit_Schlechtweg msg))
    (cl:cons ':ESP_v_Signal (ESP_v_Signal msg))
    (cl:cons ':ASR_Tastung_passiv (ASR_Tastung_passiv msg))
    (cl:cons ':ESP_Tastung_passiv (ESP_Tastung_passiv msg))
    (cl:cons ':ESP_Systemstatus (ESP_Systemstatus msg))
    (cl:cons ':ASR_Schalteingriff (ASR_Schalteingriff msg))
    (cl:cons ':ESP_QBit_v_Signal (ESP_QBit_v_Signal msg))
    (cl:cons ':ABS_Bremsung (ABS_Bremsung msg))
    (cl:cons ':ASR_Anf (ASR_Anf msg))
    (cl:cons ':MSR_Anf (MSR_Anf msg))
    (cl:cons ':EBV_Eingriff (EBV_Eingriff msg))
    (cl:cons ':EDS_Eingriff (EDS_Eingriff msg))
    (cl:cons ':ESP_Eingriff (ESP_Eingriff msg))
    (cl:cons ':ESP_ASP (ESP_ASP msg))
    (cl:cons ':ESC_Neutralschaltung (ESC_Neutralschaltung msg))
))
