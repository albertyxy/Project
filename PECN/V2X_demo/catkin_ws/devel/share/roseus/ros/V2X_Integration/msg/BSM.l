;; Auto-generated. Do not edit!


(when (boundp 'V2X_Integration::BSM)
  (if (not (find-package "V2X_INTEGRATION"))
    (make-package "V2X_INTEGRATION"))
  (shadow 'BSM (find-package "V2X_INTEGRATION")))
(unless (find-package "V2X_INTEGRATION::BSM")
  (make-package "V2X_INTEGRATION::BSM"))

(in-package "ROS")
;;//! \htmlinclude BSM.msg.html


(defclass V2X_Integration::BSM
  :super ros::object
  :slots (_id _sec_mark _message_count _latitude _longtitude _elevation _pos_accuracy_semi_major _pos_accuracy_semi_minor _pos_accuracy_orientation _lateral_acceleration _longitudinal_acceleration _vert_acceleration _yaw_acceleration _transmission_state _response_type _light_use _siren_use _events _lights _confidence_position _confidence_elevation _vehicle_class _vehicle_fuel_type _heading _speed _angle _vehicle_width _vehicle_lenth _vehicle_height _brake_padel _wheel_brakes _traction _abs _scs _brake_boost _aux_brakes ))

(defmethod V2X_Integration::BSM
  (:init
   (&key
    ((:id __id) "")
    ((:sec_mark __sec_mark) 0.0)
    ((:message_count __message_count) 0)
    ((:latitude __latitude) 0.0)
    ((:longtitude __longtitude) 0.0)
    ((:elevation __elevation) 0.0)
    ((:pos_accuracy_semi_major __pos_accuracy_semi_major) 0.0)
    ((:pos_accuracy_semi_minor __pos_accuracy_semi_minor) 0.0)
    ((:pos_accuracy_orientation __pos_accuracy_orientation) 0.0)
    ((:lateral_acceleration __lateral_acceleration) 0.0)
    ((:longitudinal_acceleration __longitudinal_acceleration) 0.0)
    ((:vert_acceleration __vert_acceleration) 0.0)
    ((:yaw_acceleration __yaw_acceleration) 0.0)
    ((:transmission_state __transmission_state) 0)
    ((:response_type __response_type) 0)
    ((:light_use __light_use) 0)
    ((:siren_use __siren_use) 0)
    ((:events __events) 0)
    ((:lights __lights) 0)
    ((:confidence_position __confidence_position) 0)
    ((:confidence_elevation __confidence_elevation) 0)
    ((:vehicle_class __vehicle_class) 0)
    ((:vehicle_fuel_type __vehicle_fuel_type) 0)
    ((:heading __heading) 0.0)
    ((:speed __speed) 0.0)
    ((:angle __angle) 0)
    ((:vehicle_width __vehicle_width) 0.0)
    ((:vehicle_lenth __vehicle_lenth) 0.0)
    ((:vehicle_height __vehicle_height) 0.0)
    ((:brake_padel __brake_padel) 0)
    ((:wheel_brakes __wheel_brakes) 0)
    ((:traction __traction) 0)
    ((:abs __abs) 0)
    ((:scs __scs) 0)
    ((:brake_boost __brake_boost) 0)
    ((:aux_brakes __aux_brakes) 0)
    )
   (send-super :init)
   (setq _id (string __id))
   (setq _sec_mark (float __sec_mark))
   (setq _message_count (round __message_count))
   (setq _latitude (float __latitude))
   (setq _longtitude (float __longtitude))
   (setq _elevation (float __elevation))
   (setq _pos_accuracy_semi_major (float __pos_accuracy_semi_major))
   (setq _pos_accuracy_semi_minor (float __pos_accuracy_semi_minor))
   (setq _pos_accuracy_orientation (float __pos_accuracy_orientation))
   (setq _lateral_acceleration (float __lateral_acceleration))
   (setq _longitudinal_acceleration (float __longitudinal_acceleration))
   (setq _vert_acceleration (float __vert_acceleration))
   (setq _yaw_acceleration (float __yaw_acceleration))
   (setq _transmission_state (round __transmission_state))
   (setq _response_type (round __response_type))
   (setq _light_use (round __light_use))
   (setq _siren_use (round __siren_use))
   (setq _events (round __events))
   (setq _lights (round __lights))
   (setq _confidence_position (round __confidence_position))
   (setq _confidence_elevation (round __confidence_elevation))
   (setq _vehicle_class (round __vehicle_class))
   (setq _vehicle_fuel_type (round __vehicle_fuel_type))
   (setq _heading (float __heading))
   (setq _speed (float __speed))
   (setq _angle (round __angle))
   (setq _vehicle_width (float __vehicle_width))
   (setq _vehicle_lenth (float __vehicle_lenth))
   (setq _vehicle_height (float __vehicle_height))
   (setq _brake_padel (round __brake_padel))
   (setq _wheel_brakes (round __wheel_brakes))
   (setq _traction (round __traction))
   (setq _abs (round __abs))
   (setq _scs (round __scs))
   (setq _brake_boost (round __brake_boost))
   (setq _aux_brakes (round __aux_brakes))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:sec_mark
   (&optional __sec_mark)
   (if __sec_mark (setq _sec_mark __sec_mark)) _sec_mark)
  (:message_count
   (&optional __message_count)
   (if __message_count (setq _message_count __message_count)) _message_count)
  (:latitude
   (&optional __latitude)
   (if __latitude (setq _latitude __latitude)) _latitude)
  (:longtitude
   (&optional __longtitude)
   (if __longtitude (setq _longtitude __longtitude)) _longtitude)
  (:elevation
   (&optional __elevation)
   (if __elevation (setq _elevation __elevation)) _elevation)
  (:pos_accuracy_semi_major
   (&optional __pos_accuracy_semi_major)
   (if __pos_accuracy_semi_major (setq _pos_accuracy_semi_major __pos_accuracy_semi_major)) _pos_accuracy_semi_major)
  (:pos_accuracy_semi_minor
   (&optional __pos_accuracy_semi_minor)
   (if __pos_accuracy_semi_minor (setq _pos_accuracy_semi_minor __pos_accuracy_semi_minor)) _pos_accuracy_semi_minor)
  (:pos_accuracy_orientation
   (&optional __pos_accuracy_orientation)
   (if __pos_accuracy_orientation (setq _pos_accuracy_orientation __pos_accuracy_orientation)) _pos_accuracy_orientation)
  (:lateral_acceleration
   (&optional __lateral_acceleration)
   (if __lateral_acceleration (setq _lateral_acceleration __lateral_acceleration)) _lateral_acceleration)
  (:longitudinal_acceleration
   (&optional __longitudinal_acceleration)
   (if __longitudinal_acceleration (setq _longitudinal_acceleration __longitudinal_acceleration)) _longitudinal_acceleration)
  (:vert_acceleration
   (&optional __vert_acceleration)
   (if __vert_acceleration (setq _vert_acceleration __vert_acceleration)) _vert_acceleration)
  (:yaw_acceleration
   (&optional __yaw_acceleration)
   (if __yaw_acceleration (setq _yaw_acceleration __yaw_acceleration)) _yaw_acceleration)
  (:transmission_state
   (&optional __transmission_state)
   (if __transmission_state (setq _transmission_state __transmission_state)) _transmission_state)
  (:response_type
   (&optional __response_type)
   (if __response_type (setq _response_type __response_type)) _response_type)
  (:light_use
   (&optional __light_use)
   (if __light_use (setq _light_use __light_use)) _light_use)
  (:siren_use
   (&optional __siren_use)
   (if __siren_use (setq _siren_use __siren_use)) _siren_use)
  (:events
   (&optional __events)
   (if __events (setq _events __events)) _events)
  (:lights
   (&optional __lights)
   (if __lights (setq _lights __lights)) _lights)
  (:confidence_position
   (&optional __confidence_position)
   (if __confidence_position (setq _confidence_position __confidence_position)) _confidence_position)
  (:confidence_elevation
   (&optional __confidence_elevation)
   (if __confidence_elevation (setq _confidence_elevation __confidence_elevation)) _confidence_elevation)
  (:vehicle_class
   (&optional __vehicle_class)
   (if __vehicle_class (setq _vehicle_class __vehicle_class)) _vehicle_class)
  (:vehicle_fuel_type
   (&optional __vehicle_fuel_type)
   (if __vehicle_fuel_type (setq _vehicle_fuel_type __vehicle_fuel_type)) _vehicle_fuel_type)
  (:heading
   (&optional __heading)
   (if __heading (setq _heading __heading)) _heading)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:vehicle_width
   (&optional __vehicle_width)
   (if __vehicle_width (setq _vehicle_width __vehicle_width)) _vehicle_width)
  (:vehicle_lenth
   (&optional __vehicle_lenth)
   (if __vehicle_lenth (setq _vehicle_lenth __vehicle_lenth)) _vehicle_lenth)
  (:vehicle_height
   (&optional __vehicle_height)
   (if __vehicle_height (setq _vehicle_height __vehicle_height)) _vehicle_height)
  (:brake_padel
   (&optional __brake_padel)
   (if __brake_padel (setq _brake_padel __brake_padel)) _brake_padel)
  (:wheel_brakes
   (&optional __wheel_brakes)
   (if __wheel_brakes (setq _wheel_brakes __wheel_brakes)) _wheel_brakes)
  (:traction
   (&optional __traction)
   (if __traction (setq _traction __traction)) _traction)
  (:abs
   (&optional __abs)
   (if __abs (setq _abs __abs)) _abs)
  (:scs
   (&optional __scs)
   (if __scs (setq _scs __scs)) _scs)
  (:brake_boost
   (&optional __brake_boost)
   (if __brake_boost (setq _brake_boost __brake_boost)) _brake_boost)
  (:aux_brakes
   (&optional __aux_brakes)
   (if __aux_brakes (setq _aux_brakes __aux_brakes)) _aux_brakes)
  (:serialization-length
   ()
   (+
    ;; string _id
    4 (length _id)
    ;; float32 _sec_mark
    4
    ;; int16 _message_count
    2
    ;; float32 _latitude
    4
    ;; float32 _longtitude
    4
    ;; float32 _elevation
    4
    ;; float32 _pos_accuracy_semi_major
    4
    ;; float32 _pos_accuracy_semi_minor
    4
    ;; float32 _pos_accuracy_orientation
    4
    ;; float32 _lateral_acceleration
    4
    ;; float32 _longitudinal_acceleration
    4
    ;; float32 _vert_acceleration
    4
    ;; float32 _yaw_acceleration
    4
    ;; uint8 _transmission_state
    1
    ;; uint8 _response_type
    1
    ;; uint8 _light_use
    1
    ;; uint8 _siren_use
    1
    ;; uint8 _events
    1
    ;; uint8 _lights
    1
    ;; uint8 _confidence_position
    1
    ;; uint8 _confidence_elevation
    1
    ;; uint8 _vehicle_class
    1
    ;; uint8 _vehicle_fuel_type
    1
    ;; float32 _heading
    4
    ;; float32 _speed
    4
    ;; int16 _angle
    2
    ;; float32 _vehicle_width
    4
    ;; float32 _vehicle_lenth
    4
    ;; float32 _vehicle_height
    4
    ;; uint8 _brake_padel
    1
    ;; uint8 _wheel_brakes
    1
    ;; uint8 _traction
    1
    ;; uint8 _abs
    1
    ;; uint8 _scs
    1
    ;; uint8 _brake_boost
    1
    ;; uint8 _aux_brakes
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _id
       (write-long (length _id) s) (princ _id s)
     ;; float32 _sec_mark
       (sys::poke _sec_mark (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int16 _message_count
       (write-word _message_count s)
     ;; float32 _latitude
       (sys::poke _latitude (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _longtitude
       (sys::poke _longtitude (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _elevation
       (sys::poke _elevation (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _pos_accuracy_semi_major
       (sys::poke _pos_accuracy_semi_major (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _pos_accuracy_semi_minor
       (sys::poke _pos_accuracy_semi_minor (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _pos_accuracy_orientation
       (sys::poke _pos_accuracy_orientation (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _lateral_acceleration
       (sys::poke _lateral_acceleration (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _longitudinal_acceleration
       (sys::poke _longitudinal_acceleration (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _vert_acceleration
       (sys::poke _vert_acceleration (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _yaw_acceleration
       (sys::poke _yaw_acceleration (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; uint8 _transmission_state
       (write-byte _transmission_state s)
     ;; uint8 _response_type
       (write-byte _response_type s)
     ;; uint8 _light_use
       (write-byte _light_use s)
     ;; uint8 _siren_use
       (write-byte _siren_use s)
     ;; uint8 _events
       (write-byte _events s)
     ;; uint8 _lights
       (write-byte _lights s)
     ;; uint8 _confidence_position
       (write-byte _confidence_position s)
     ;; uint8 _confidence_elevation
       (write-byte _confidence_elevation s)
     ;; uint8 _vehicle_class
       (write-byte _vehicle_class s)
     ;; uint8 _vehicle_fuel_type
       (write-byte _vehicle_fuel_type s)
     ;; float32 _heading
       (sys::poke _heading (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int16 _angle
       (write-word _angle s)
     ;; float32 _vehicle_width
       (sys::poke _vehicle_width (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _vehicle_lenth
       (sys::poke _vehicle_lenth (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _vehicle_height
       (sys::poke _vehicle_height (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; uint8 _brake_padel
       (write-byte _brake_padel s)
     ;; uint8 _wheel_brakes
       (write-byte _wheel_brakes s)
     ;; uint8 _traction
       (write-byte _traction s)
     ;; uint8 _abs
       (write-byte _abs s)
     ;; uint8 _scs
       (write-byte _scs s)
     ;; uint8 _brake_boost
       (write-byte _brake_boost s)
     ;; uint8 _aux_brakes
       (write-byte _aux_brakes s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _id
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _id (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _sec_mark
     (setq _sec_mark (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int16 _message_count
     (setq _message_count (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; float32 _latitude
     (setq _latitude (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _longtitude
     (setq _longtitude (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _elevation
     (setq _elevation (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _pos_accuracy_semi_major
     (setq _pos_accuracy_semi_major (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _pos_accuracy_semi_minor
     (setq _pos_accuracy_semi_minor (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _pos_accuracy_orientation
     (setq _pos_accuracy_orientation (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _lateral_acceleration
     (setq _lateral_acceleration (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _longitudinal_acceleration
     (setq _longitudinal_acceleration (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _vert_acceleration
     (setq _vert_acceleration (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _yaw_acceleration
     (setq _yaw_acceleration (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; uint8 _transmission_state
     (setq _transmission_state (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _response_type
     (setq _response_type (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _light_use
     (setq _light_use (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _siren_use
     (setq _siren_use (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _events
     (setq _events (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _lights
     (setq _lights (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _confidence_position
     (setq _confidence_position (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _confidence_elevation
     (setq _confidence_elevation (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _vehicle_class
     (setq _vehicle_class (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _vehicle_fuel_type
     (setq _vehicle_fuel_type (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float32 _heading
     (setq _heading (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _speed
     (setq _speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int16 _angle
     (setq _angle (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; float32 _vehicle_width
     (setq _vehicle_width (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _vehicle_lenth
     (setq _vehicle_lenth (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _vehicle_height
     (setq _vehicle_height (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; uint8 _brake_padel
     (setq _brake_padel (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _wheel_brakes
     (setq _wheel_brakes (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _traction
     (setq _traction (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _abs
     (setq _abs (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _scs
     (setq _scs (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _brake_boost
     (setq _brake_boost (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _aux_brakes
     (setq _aux_brakes (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get V2X_Integration::BSM :md5sum-) "e6940b8bdce7382d047211cc39f10e12")
(setf (get V2X_Integration::BSM :datatype-) "V2X_Integration/BSM")
(setf (get V2X_Integration::BSM :definition-)
      "string id
float32 sec_mark
int16 message_count
float32 latitude
float32 longtitude
float32 elevation
float32 pos_accuracy_semi_major
float32 pos_accuracy_semi_minor
float32 pos_accuracy_orientation
float32 lateral_acceleration
float32 longitudinal_acceleration
float32 vert_acceleration
float32 yaw_acceleration
uint8 transmission_state
uint8 response_type
uint8 light_use
uint8 siren_use
uint8 events
uint8 lights
uint8 confidence_position
uint8 confidence_elevation
uint8 vehicle_class
uint8 vehicle_fuel_type
float32 heading
float32 speed
int16 angle
float32 vehicle_width
float32 vehicle_lenth
float32 vehicle_height
uint8 brake_padel
uint8 wheel_brakes
uint8 traction
uint8 abs
uint8 scs
uint8 brake_boost
uint8 aux_brakes



























")



(provide :V2X_Integration/BSM "e6940b8bdce7382d047211cc39f10e12")


