;; Auto-generated. Do not edit!


(when (boundp 'V2X_Integration::ESP_21_Msg)
  (if (not (find-package "V2X_INTEGRATION"))
    (make-package "V2X_INTEGRATION"))
  (shadow 'ESP_21_Msg (find-package "V2X_INTEGRATION")))
(unless (find-package "V2X_INTEGRATION::ESP_21_MSG")
  (make-package "V2X_INTEGRATION::ESP_21_MSG"))

(in-package "ROS")
;;//! \htmlinclude ESP_21_Msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass V2X_Integration::ESP_21_Msg
  :super ros::object
  :slots (_header _ESP_21_CRC _ESP_21_BZ _BR_Eingriffsmoment _ESP_Diagnose _ESC_v_Signal_Qualifier_High_Low _ESP_Vorsteuerung _OBD_Schlechtweg _OBD_QBit_Schlechtweg _ESP_v_Signal _ASR_Tastung_passiv _ESP_Tastung_passiv _ESP_Systemstatus _ASR_Schalteingriff _ESP_QBit_v_Signal _ABS_Bremsung _ASR_Anf _MSR_Anf _EBV_Eingriff _EDS_Eingriff _ESP_Eingriff _ESP_ASP _ESC_Neutralschaltung ))

(defmethod V2X_Integration::ESP_21_Msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:ESP_21_CRC __ESP_21_CRC) 0)
    ((:ESP_21_BZ __ESP_21_BZ) 0)
    ((:BR_Eingriffsmoment __BR_Eingriffsmoment) 0)
    ((:ESP_Diagnose __ESP_Diagnose) 0)
    ((:ESC_v_Signal_Qualifier_High_Low __ESC_v_Signal_Qualifier_High_Low) 0)
    ((:ESP_Vorsteuerung __ESP_Vorsteuerung) 0)
    ((:OBD_Schlechtweg __OBD_Schlechtweg) 0)
    ((:OBD_QBit_Schlechtweg __OBD_QBit_Schlechtweg) 0)
    ((:ESP_v_Signal __ESP_v_Signal) 0.0)
    ((:ASR_Tastung_passiv __ASR_Tastung_passiv) 0)
    ((:ESP_Tastung_passiv __ESP_Tastung_passiv) 0)
    ((:ESP_Systemstatus __ESP_Systemstatus) 0)
    ((:ASR_Schalteingriff __ASR_Schalteingriff) 0)
    ((:ESP_QBit_v_Signal __ESP_QBit_v_Signal) 0)
    ((:ABS_Bremsung __ABS_Bremsung) 0)
    ((:ASR_Anf __ASR_Anf) 0)
    ((:MSR_Anf __MSR_Anf) 0)
    ((:EBV_Eingriff __EBV_Eingriff) 0)
    ((:EDS_Eingriff __EDS_Eingriff) 0)
    ((:ESP_Eingriff __ESP_Eingriff) 0)
    ((:ESP_ASP __ESP_ASP) 0)
    ((:ESC_Neutralschaltung __ESC_Neutralschaltung) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _ESP_21_CRC (round __ESP_21_CRC))
   (setq _ESP_21_BZ (round __ESP_21_BZ))
   (setq _BR_Eingriffsmoment (round __BR_Eingriffsmoment))
   (setq _ESP_Diagnose (round __ESP_Diagnose))
   (setq _ESC_v_Signal_Qualifier_High_Low (round __ESC_v_Signal_Qualifier_High_Low))
   (setq _ESP_Vorsteuerung (round __ESP_Vorsteuerung))
   (setq _OBD_Schlechtweg (round __OBD_Schlechtweg))
   (setq _OBD_QBit_Schlechtweg (round __OBD_QBit_Schlechtweg))
   (setq _ESP_v_Signal (float __ESP_v_Signal))
   (setq _ASR_Tastung_passiv (round __ASR_Tastung_passiv))
   (setq _ESP_Tastung_passiv (round __ESP_Tastung_passiv))
   (setq _ESP_Systemstatus (round __ESP_Systemstatus))
   (setq _ASR_Schalteingriff (round __ASR_Schalteingriff))
   (setq _ESP_QBit_v_Signal (round __ESP_QBit_v_Signal))
   (setq _ABS_Bremsung (round __ABS_Bremsung))
   (setq _ASR_Anf (round __ASR_Anf))
   (setq _MSR_Anf (round __MSR_Anf))
   (setq _EBV_Eingriff (round __EBV_Eingriff))
   (setq _EDS_Eingriff (round __EDS_Eingriff))
   (setq _ESP_Eingriff (round __ESP_Eingriff))
   (setq _ESP_ASP (round __ESP_ASP))
   (setq _ESC_Neutralschaltung (round __ESC_Neutralschaltung))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:ESP_21_CRC
   (&optional __ESP_21_CRC)
   (if __ESP_21_CRC (setq _ESP_21_CRC __ESP_21_CRC)) _ESP_21_CRC)
  (:ESP_21_BZ
   (&optional __ESP_21_BZ)
   (if __ESP_21_BZ (setq _ESP_21_BZ __ESP_21_BZ)) _ESP_21_BZ)
  (:BR_Eingriffsmoment
   (&optional __BR_Eingriffsmoment)
   (if __BR_Eingriffsmoment (setq _BR_Eingriffsmoment __BR_Eingriffsmoment)) _BR_Eingriffsmoment)
  (:ESP_Diagnose
   (&optional __ESP_Diagnose)
   (if __ESP_Diagnose (setq _ESP_Diagnose __ESP_Diagnose)) _ESP_Diagnose)
  (:ESC_v_Signal_Qualifier_High_Low
   (&optional __ESC_v_Signal_Qualifier_High_Low)
   (if __ESC_v_Signal_Qualifier_High_Low (setq _ESC_v_Signal_Qualifier_High_Low __ESC_v_Signal_Qualifier_High_Low)) _ESC_v_Signal_Qualifier_High_Low)
  (:ESP_Vorsteuerung
   (&optional __ESP_Vorsteuerung)
   (if __ESP_Vorsteuerung (setq _ESP_Vorsteuerung __ESP_Vorsteuerung)) _ESP_Vorsteuerung)
  (:OBD_Schlechtweg
   (&optional __OBD_Schlechtweg)
   (if __OBD_Schlechtweg (setq _OBD_Schlechtweg __OBD_Schlechtweg)) _OBD_Schlechtweg)
  (:OBD_QBit_Schlechtweg
   (&optional __OBD_QBit_Schlechtweg)
   (if __OBD_QBit_Schlechtweg (setq _OBD_QBit_Schlechtweg __OBD_QBit_Schlechtweg)) _OBD_QBit_Schlechtweg)
  (:ESP_v_Signal
   (&optional __ESP_v_Signal)
   (if __ESP_v_Signal (setq _ESP_v_Signal __ESP_v_Signal)) _ESP_v_Signal)
  (:ASR_Tastung_passiv
   (&optional __ASR_Tastung_passiv)
   (if __ASR_Tastung_passiv (setq _ASR_Tastung_passiv __ASR_Tastung_passiv)) _ASR_Tastung_passiv)
  (:ESP_Tastung_passiv
   (&optional __ESP_Tastung_passiv)
   (if __ESP_Tastung_passiv (setq _ESP_Tastung_passiv __ESP_Tastung_passiv)) _ESP_Tastung_passiv)
  (:ESP_Systemstatus
   (&optional __ESP_Systemstatus)
   (if __ESP_Systemstatus (setq _ESP_Systemstatus __ESP_Systemstatus)) _ESP_Systemstatus)
  (:ASR_Schalteingriff
   (&optional __ASR_Schalteingriff)
   (if __ASR_Schalteingriff (setq _ASR_Schalteingriff __ASR_Schalteingriff)) _ASR_Schalteingriff)
  (:ESP_QBit_v_Signal
   (&optional __ESP_QBit_v_Signal)
   (if __ESP_QBit_v_Signal (setq _ESP_QBit_v_Signal __ESP_QBit_v_Signal)) _ESP_QBit_v_Signal)
  (:ABS_Bremsung
   (&optional __ABS_Bremsung)
   (if __ABS_Bremsung (setq _ABS_Bremsung __ABS_Bremsung)) _ABS_Bremsung)
  (:ASR_Anf
   (&optional __ASR_Anf)
   (if __ASR_Anf (setq _ASR_Anf __ASR_Anf)) _ASR_Anf)
  (:MSR_Anf
   (&optional __MSR_Anf)
   (if __MSR_Anf (setq _MSR_Anf __MSR_Anf)) _MSR_Anf)
  (:EBV_Eingriff
   (&optional __EBV_Eingriff)
   (if __EBV_Eingriff (setq _EBV_Eingriff __EBV_Eingriff)) _EBV_Eingriff)
  (:EDS_Eingriff
   (&optional __EDS_Eingriff)
   (if __EDS_Eingriff (setq _EDS_Eingriff __EDS_Eingriff)) _EDS_Eingriff)
  (:ESP_Eingriff
   (&optional __ESP_Eingriff)
   (if __ESP_Eingriff (setq _ESP_Eingriff __ESP_Eingriff)) _ESP_Eingriff)
  (:ESP_ASP
   (&optional __ESP_ASP)
   (if __ESP_ASP (setq _ESP_ASP __ESP_ASP)) _ESP_ASP)
  (:ESC_Neutralschaltung
   (&optional __ESC_Neutralschaltung)
   (if __ESC_Neutralschaltung (setq _ESC_Neutralschaltung __ESC_Neutralschaltung)) _ESC_Neutralschaltung)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint16 _ESP_21_CRC
    2
    ;; uint8 _ESP_21_BZ
    1
    ;; int16 _BR_Eingriffsmoment
    2
    ;; uint8 _ESP_Diagnose
    1
    ;; uint8 _ESC_v_Signal_Qualifier_High_Low
    1
    ;; uint8 _ESP_Vorsteuerung
    1
    ;; uint8 _OBD_Schlechtweg
    1
    ;; uint8 _OBD_QBit_Schlechtweg
    1
    ;; float32 _ESP_v_Signal
    4
    ;; uint8 _ASR_Tastung_passiv
    1
    ;; uint8 _ESP_Tastung_passiv
    1
    ;; uint8 _ESP_Systemstatus
    1
    ;; uint8 _ASR_Schalteingriff
    1
    ;; uint8 _ESP_QBit_v_Signal
    1
    ;; uint8 _ABS_Bremsung
    1
    ;; uint8 _ASR_Anf
    1
    ;; uint8 _MSR_Anf
    1
    ;; uint8 _EBV_Eingriff
    1
    ;; uint8 _EDS_Eingriff
    1
    ;; uint8 _ESP_Eingriff
    1
    ;; uint8 _ESP_ASP
    1
    ;; uint8 _ESC_Neutralschaltung
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint16 _ESP_21_CRC
       (write-word _ESP_21_CRC s)
     ;; uint8 _ESP_21_BZ
       (write-byte _ESP_21_BZ s)
     ;; int16 _BR_Eingriffsmoment
       (write-word _BR_Eingriffsmoment s)
     ;; uint8 _ESP_Diagnose
       (write-byte _ESP_Diagnose s)
     ;; uint8 _ESC_v_Signal_Qualifier_High_Low
       (write-byte _ESC_v_Signal_Qualifier_High_Low s)
     ;; uint8 _ESP_Vorsteuerung
       (write-byte _ESP_Vorsteuerung s)
     ;; uint8 _OBD_Schlechtweg
       (write-byte _OBD_Schlechtweg s)
     ;; uint8 _OBD_QBit_Schlechtweg
       (write-byte _OBD_QBit_Schlechtweg s)
     ;; float32 _ESP_v_Signal
       (sys::poke _ESP_v_Signal (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; uint8 _ASR_Tastung_passiv
       (write-byte _ASR_Tastung_passiv s)
     ;; uint8 _ESP_Tastung_passiv
       (write-byte _ESP_Tastung_passiv s)
     ;; uint8 _ESP_Systemstatus
       (write-byte _ESP_Systemstatus s)
     ;; uint8 _ASR_Schalteingriff
       (write-byte _ASR_Schalteingriff s)
     ;; uint8 _ESP_QBit_v_Signal
       (write-byte _ESP_QBit_v_Signal s)
     ;; uint8 _ABS_Bremsung
       (write-byte _ABS_Bremsung s)
     ;; uint8 _ASR_Anf
       (write-byte _ASR_Anf s)
     ;; uint8 _MSR_Anf
       (write-byte _MSR_Anf s)
     ;; uint8 _EBV_Eingriff
       (write-byte _EBV_Eingriff s)
     ;; uint8 _EDS_Eingriff
       (write-byte _EDS_Eingriff s)
     ;; uint8 _ESP_Eingriff
       (write-byte _ESP_Eingriff s)
     ;; uint8 _ESP_ASP
       (write-byte _ESP_ASP s)
     ;; uint8 _ESC_Neutralschaltung
       (write-byte _ESC_Neutralschaltung s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint16 _ESP_21_CRC
     (setq _ESP_21_CRC (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint8 _ESP_21_BZ
     (setq _ESP_21_BZ (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; int16 _BR_Eingriffsmoment
     (setq _BR_Eingriffsmoment (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint8 _ESP_Diagnose
     (setq _ESP_Diagnose (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _ESC_v_Signal_Qualifier_High_Low
     (setq _ESC_v_Signal_Qualifier_High_Low (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _ESP_Vorsteuerung
     (setq _ESP_Vorsteuerung (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _OBD_Schlechtweg
     (setq _OBD_Schlechtweg (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _OBD_QBit_Schlechtweg
     (setq _OBD_QBit_Schlechtweg (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float32 _ESP_v_Signal
     (setq _ESP_v_Signal (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; uint8 _ASR_Tastung_passiv
     (setq _ASR_Tastung_passiv (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _ESP_Tastung_passiv
     (setq _ESP_Tastung_passiv (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _ESP_Systemstatus
     (setq _ESP_Systemstatus (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _ASR_Schalteingriff
     (setq _ASR_Schalteingriff (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _ESP_QBit_v_Signal
     (setq _ESP_QBit_v_Signal (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _ABS_Bremsung
     (setq _ABS_Bremsung (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _ASR_Anf
     (setq _ASR_Anf (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _MSR_Anf
     (setq _MSR_Anf (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _EBV_Eingriff
     (setq _EBV_Eingriff (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _EDS_Eingriff
     (setq _EDS_Eingriff (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _ESP_Eingriff
     (setq _ESP_Eingriff (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _ESP_ASP
     (setq _ESP_ASP (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _ESC_Neutralschaltung
     (setq _ESC_Neutralschaltung (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get V2X_Integration::ESP_21_Msg :md5sum-) "14034e15be32d792bb36bad51c5aaa1b")
(setf (get V2X_Integration::ESP_21_Msg :datatype-) "V2X_Integration/ESP_21_Msg")
(setf (get V2X_Integration::ESP_21_Msg :definition-)
      "Header header
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

")



(provide :V2X_Integration/ESP_21_Msg "14034e15be32d792bb36bad51c5aaa1b")


