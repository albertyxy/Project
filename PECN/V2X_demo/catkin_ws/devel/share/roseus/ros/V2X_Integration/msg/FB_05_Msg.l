;; Auto-generated. Do not edit!


(when (boundp 'V2X_Integration::FB_05_Msg)
  (if (not (find-package "V2X_INTEGRATION"))
    (make-package "V2X_INTEGRATION"))
  (shadow 'FB_05_Msg (find-package "V2X_INTEGRATION")))
(unless (find-package "V2X_INTEGRATION::FB_05_MSG")
  (make-package "V2X_INTEGRATION::FB_05_MSG"))

(in-package "ROS")
;;//! \htmlinclude FB_05_Msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass V2X_Integration::FB_05_Msg
  :super ros::object
  :slots (_header _FB_Kopfrotation_Gier_Guete _FB_Kopfposition_Z_Guete _FB_Kopfposition_Y_Guete _FB_Kopfposition_X_Guete _FB_Kopfrotation_Gier _FB_Kopfposition_Z _FB_Kopfposition_Y _FB_Kopfposition_X ))

(defmethod V2X_Integration::FB_05_Msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:FB_Kopfrotation_Gier_Guete __FB_Kopfrotation_Gier_Guete) 0.0)
    ((:FB_Kopfposition_Z_Guete __FB_Kopfposition_Z_Guete) 0.0)
    ((:FB_Kopfposition_Y_Guete __FB_Kopfposition_Y_Guete) 0.0)
    ((:FB_Kopfposition_X_Guete __FB_Kopfposition_X_Guete) 0.0)
    ((:FB_Kopfrotation_Gier __FB_Kopfrotation_Gier) 0.0)
    ((:FB_Kopfposition_Z __FB_Kopfposition_Z) 0.0)
    ((:FB_Kopfposition_Y __FB_Kopfposition_Y) 0.0)
    ((:FB_Kopfposition_X __FB_Kopfposition_X) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _FB_Kopfrotation_Gier_Guete (float __FB_Kopfrotation_Gier_Guete))
   (setq _FB_Kopfposition_Z_Guete (float __FB_Kopfposition_Z_Guete))
   (setq _FB_Kopfposition_Y_Guete (float __FB_Kopfposition_Y_Guete))
   (setq _FB_Kopfposition_X_Guete (float __FB_Kopfposition_X_Guete))
   (setq _FB_Kopfrotation_Gier (float __FB_Kopfrotation_Gier))
   (setq _FB_Kopfposition_Z (float __FB_Kopfposition_Z))
   (setq _FB_Kopfposition_Y (float __FB_Kopfposition_Y))
   (setq _FB_Kopfposition_X (float __FB_Kopfposition_X))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:FB_Kopfrotation_Gier_Guete
   (&optional __FB_Kopfrotation_Gier_Guete)
   (if __FB_Kopfrotation_Gier_Guete (setq _FB_Kopfrotation_Gier_Guete __FB_Kopfrotation_Gier_Guete)) _FB_Kopfrotation_Gier_Guete)
  (:FB_Kopfposition_Z_Guete
   (&optional __FB_Kopfposition_Z_Guete)
   (if __FB_Kopfposition_Z_Guete (setq _FB_Kopfposition_Z_Guete __FB_Kopfposition_Z_Guete)) _FB_Kopfposition_Z_Guete)
  (:FB_Kopfposition_Y_Guete
   (&optional __FB_Kopfposition_Y_Guete)
   (if __FB_Kopfposition_Y_Guete (setq _FB_Kopfposition_Y_Guete __FB_Kopfposition_Y_Guete)) _FB_Kopfposition_Y_Guete)
  (:FB_Kopfposition_X_Guete
   (&optional __FB_Kopfposition_X_Guete)
   (if __FB_Kopfposition_X_Guete (setq _FB_Kopfposition_X_Guete __FB_Kopfposition_X_Guete)) _FB_Kopfposition_X_Guete)
  (:FB_Kopfrotation_Gier
   (&optional __FB_Kopfrotation_Gier)
   (if __FB_Kopfrotation_Gier (setq _FB_Kopfrotation_Gier __FB_Kopfrotation_Gier)) _FB_Kopfrotation_Gier)
  (:FB_Kopfposition_Z
   (&optional __FB_Kopfposition_Z)
   (if __FB_Kopfposition_Z (setq _FB_Kopfposition_Z __FB_Kopfposition_Z)) _FB_Kopfposition_Z)
  (:FB_Kopfposition_Y
   (&optional __FB_Kopfposition_Y)
   (if __FB_Kopfposition_Y (setq _FB_Kopfposition_Y __FB_Kopfposition_Y)) _FB_Kopfposition_Y)
  (:FB_Kopfposition_X
   (&optional __FB_Kopfposition_X)
   (if __FB_Kopfposition_X (setq _FB_Kopfposition_X __FB_Kopfposition_X)) _FB_Kopfposition_X)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _FB_Kopfrotation_Gier_Guete
    4
    ;; float32 _FB_Kopfposition_Z_Guete
    4
    ;; float32 _FB_Kopfposition_Y_Guete
    4
    ;; float32 _FB_Kopfposition_X_Guete
    4
    ;; float32 _FB_Kopfrotation_Gier
    4
    ;; float32 _FB_Kopfposition_Z
    4
    ;; float32 _FB_Kopfposition_Y
    4
    ;; float32 _FB_Kopfposition_X
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _FB_Kopfrotation_Gier_Guete
       (sys::poke _FB_Kopfrotation_Gier_Guete (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _FB_Kopfposition_Z_Guete
       (sys::poke _FB_Kopfposition_Z_Guete (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _FB_Kopfposition_Y_Guete
       (sys::poke _FB_Kopfposition_Y_Guete (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _FB_Kopfposition_X_Guete
       (sys::poke _FB_Kopfposition_X_Guete (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _FB_Kopfrotation_Gier
       (sys::poke _FB_Kopfrotation_Gier (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _FB_Kopfposition_Z
       (sys::poke _FB_Kopfposition_Z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _FB_Kopfposition_Y
       (sys::poke _FB_Kopfposition_Y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _FB_Kopfposition_X
       (sys::poke _FB_Kopfposition_X (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _FB_Kopfrotation_Gier_Guete
     (setq _FB_Kopfrotation_Gier_Guete (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _FB_Kopfposition_Z_Guete
     (setq _FB_Kopfposition_Z_Guete (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _FB_Kopfposition_Y_Guete
     (setq _FB_Kopfposition_Y_Guete (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _FB_Kopfposition_X_Guete
     (setq _FB_Kopfposition_X_Guete (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _FB_Kopfrotation_Gier
     (setq _FB_Kopfrotation_Gier (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _FB_Kopfposition_Z
     (setq _FB_Kopfposition_Z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _FB_Kopfposition_Y
     (setq _FB_Kopfposition_Y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _FB_Kopfposition_X
     (setq _FB_Kopfposition_X (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get V2X_Integration::FB_05_Msg :md5sum-) "e0505810bf77d4eb9eb73dfc0b88136b")
(setf (get V2X_Integration::FB_05_Msg :datatype-) "V2X_Integration/FB_05_Msg")
(setf (get V2X_Integration::FB_05_Msg :definition-)
      "Header header
float32 FB_Kopfrotation_Gier_Guete
float32 FB_Kopfposition_Z_Guete
float32 FB_Kopfposition_Y_Guete
float32 FB_Kopfposition_X_Guete
float32 FB_Kopfrotation_Gier
float32 FB_Kopfposition_Z
float32 FB_Kopfposition_Y
float32 FB_Kopfposition_X

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



(provide :V2X_Integration/FB_05_Msg "e0505810bf77d4eb9eb73dfc0b88136b")


