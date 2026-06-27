;; Auto-generated. Do not edit!


(when (boundp 'V2X_Integration::SARA_06_Msg)
  (if (not (find-package "V2X_INTEGRATION"))
    (make-package "V2X_INTEGRATION"))
  (shadow 'SARA_06_Msg (find-package "V2X_INTEGRATION")))
(unless (find-package "V2X_INTEGRATION::SARA_06_MSG")
  (make-package "V2X_INTEGRATION::SARA_06_MSG"))

(in-package "ROS")
;;//! \htmlinclude SARA_06_Msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass V2X_Integration::SARA_06_Msg
  :super ros::object
  :slots (_header _SARA_06_CRC _SARA_06_BZ _SARA_Accel_X_010 _SARA_Accel_Y_010 _SARA_Omega_Z_010 _SARA_CF_Accel_X_010 _SARA_CF_Accel_Y_010 _SARA_CF_Omega_Z_010 ))

(defmethod V2X_Integration::SARA_06_Msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:SARA_06_CRC __SARA_06_CRC) 0)
    ((:SARA_06_BZ __SARA_06_BZ) 0)
    ((:SARA_Accel_X_010 __SARA_Accel_X_010) 0.0)
    ((:SARA_Accel_Y_010 __SARA_Accel_Y_010) 0.0)
    ((:SARA_Omega_Z_010 __SARA_Omega_Z_010) 0.0)
    ((:SARA_CF_Accel_X_010 __SARA_CF_Accel_X_010) 0)
    ((:SARA_CF_Accel_Y_010 __SARA_CF_Accel_Y_010) 0)
    ((:SARA_CF_Omega_Z_010 __SARA_CF_Omega_Z_010) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _SARA_06_CRC (round __SARA_06_CRC))
   (setq _SARA_06_BZ (round __SARA_06_BZ))
   (setq _SARA_Accel_X_010 (float __SARA_Accel_X_010))
   (setq _SARA_Accel_Y_010 (float __SARA_Accel_Y_010))
   (setq _SARA_Omega_Z_010 (float __SARA_Omega_Z_010))
   (setq _SARA_CF_Accel_X_010 (round __SARA_CF_Accel_X_010))
   (setq _SARA_CF_Accel_Y_010 (round __SARA_CF_Accel_Y_010))
   (setq _SARA_CF_Omega_Z_010 (round __SARA_CF_Omega_Z_010))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:SARA_06_CRC
   (&optional __SARA_06_CRC)
   (if __SARA_06_CRC (setq _SARA_06_CRC __SARA_06_CRC)) _SARA_06_CRC)
  (:SARA_06_BZ
   (&optional __SARA_06_BZ)
   (if __SARA_06_BZ (setq _SARA_06_BZ __SARA_06_BZ)) _SARA_06_BZ)
  (:SARA_Accel_X_010
   (&optional __SARA_Accel_X_010)
   (if __SARA_Accel_X_010 (setq _SARA_Accel_X_010 __SARA_Accel_X_010)) _SARA_Accel_X_010)
  (:SARA_Accel_Y_010
   (&optional __SARA_Accel_Y_010)
   (if __SARA_Accel_Y_010 (setq _SARA_Accel_Y_010 __SARA_Accel_Y_010)) _SARA_Accel_Y_010)
  (:SARA_Omega_Z_010
   (&optional __SARA_Omega_Z_010)
   (if __SARA_Omega_Z_010 (setq _SARA_Omega_Z_010 __SARA_Omega_Z_010)) _SARA_Omega_Z_010)
  (:SARA_CF_Accel_X_010
   (&optional __SARA_CF_Accel_X_010)
   (if __SARA_CF_Accel_X_010 (setq _SARA_CF_Accel_X_010 __SARA_CF_Accel_X_010)) _SARA_CF_Accel_X_010)
  (:SARA_CF_Accel_Y_010
   (&optional __SARA_CF_Accel_Y_010)
   (if __SARA_CF_Accel_Y_010 (setq _SARA_CF_Accel_Y_010 __SARA_CF_Accel_Y_010)) _SARA_CF_Accel_Y_010)
  (:SARA_CF_Omega_Z_010
   (&optional __SARA_CF_Omega_Z_010)
   (if __SARA_CF_Omega_Z_010 (setq _SARA_CF_Omega_Z_010 __SARA_CF_Omega_Z_010)) _SARA_CF_Omega_Z_010)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint16 _SARA_06_CRC
    2
    ;; uint8 _SARA_06_BZ
    1
    ;; float32 _SARA_Accel_X_010
    4
    ;; float32 _SARA_Accel_Y_010
    4
    ;; float32 _SARA_Omega_Z_010
    4
    ;; uint8 _SARA_CF_Accel_X_010
    1
    ;; uint8 _SARA_CF_Accel_Y_010
    1
    ;; uint8 _SARA_CF_Omega_Z_010
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint16 _SARA_06_CRC
       (write-word _SARA_06_CRC s)
     ;; uint8 _SARA_06_BZ
       (write-byte _SARA_06_BZ s)
     ;; float32 _SARA_Accel_X_010
       (sys::poke _SARA_Accel_X_010 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _SARA_Accel_Y_010
       (sys::poke _SARA_Accel_Y_010 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _SARA_Omega_Z_010
       (sys::poke _SARA_Omega_Z_010 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; uint8 _SARA_CF_Accel_X_010
       (write-byte _SARA_CF_Accel_X_010 s)
     ;; uint8 _SARA_CF_Accel_Y_010
       (write-byte _SARA_CF_Accel_Y_010 s)
     ;; uint8 _SARA_CF_Omega_Z_010
       (write-byte _SARA_CF_Omega_Z_010 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint16 _SARA_06_CRC
     (setq _SARA_06_CRC (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint8 _SARA_06_BZ
     (setq _SARA_06_BZ (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float32 _SARA_Accel_X_010
     (setq _SARA_Accel_X_010 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _SARA_Accel_Y_010
     (setq _SARA_Accel_Y_010 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _SARA_Omega_Z_010
     (setq _SARA_Omega_Z_010 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; uint8 _SARA_CF_Accel_X_010
     (setq _SARA_CF_Accel_X_010 (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _SARA_CF_Accel_Y_010
     (setq _SARA_CF_Accel_Y_010 (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _SARA_CF_Omega_Z_010
     (setq _SARA_CF_Omega_Z_010 (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get V2X_Integration::SARA_06_Msg :md5sum-) "2d6f91f1b10aaef29935d4bdfc80abae")
(setf (get V2X_Integration::SARA_06_Msg :datatype-) "V2X_Integration/SARA_06_Msg")
(setf (get V2X_Integration::SARA_06_Msg :definition-)
      "Header header
uint16 SARA_06_CRC
uint8 SARA_06_BZ
float32 SARA_Accel_X_010
float32 SARA_Accel_Y_010
float32 SARA_Omega_Z_010
uint8 SARA_CF_Accel_X_010
uint8 SARA_CF_Accel_Y_010
uint8 SARA_CF_Omega_Z_010

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



(provide :V2X_Integration/SARA_06_Msg "2d6f91f1b10aaef29935d4bdfc80abae")


