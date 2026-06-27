;; Auto-generated. Do not edit!


(when (boundp 'V2X_Integration::V2X_Warning)
  (if (not (find-package "V2X_INTEGRATION"))
    (make-package "V2X_INTEGRATION"))
  (shadow 'V2X_Warning (find-package "V2X_INTEGRATION")))
(unless (find-package "V2X_INTEGRATION::V2X_WARNING")
  (make-package "V2X_INTEGRATION::V2X_WARNING"))

(in-package "ROS")
;;//! \htmlinclude V2X_Warning.msg.html


(defclass V2X_Integration::V2X_Warning
  :super ros::object
  :slots (_warning_level ))

(defmethod V2X_Integration::V2X_Warning
  (:init
   (&key
    ((:warning_level __warning_level) 0)
    )
   (send-super :init)
   (setq _warning_level (round __warning_level))
   self)
  (:warning_level
   (&optional __warning_level)
   (if __warning_level (setq _warning_level __warning_level)) _warning_level)
  (:serialization-length
   ()
   (+
    ;; uint8 _warning_level
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _warning_level
       (write-byte _warning_level s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _warning_level
     (setq _warning_level (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get V2X_Integration::V2X_Warning :md5sum-) "140cc051af28c9742e4f2dcebd133a9b")
(setf (get V2X_Integration::V2X_Warning :datatype-) "V2X_Integration/V2X_Warning")
(setf (get V2X_Integration::V2X_Warning :definition-)
      "uint8 warning_level

























")



(provide :V2X_Integration/V2X_Warning "140cc051af28c9742e4f2dcebd133a9b")


