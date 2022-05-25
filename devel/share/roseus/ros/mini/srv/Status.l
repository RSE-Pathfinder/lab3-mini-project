;; Auto-generated. Do not edit!


(when (boundp 'mini::Status)
  (if (not (find-package "MINI"))
    (make-package "MINI"))
  (shadow 'Status (find-package "MINI")))
(unless (find-package "MINI::STATUS")
  (make-package "MINI::STATUS"))
(unless (find-package "MINI::STATUSREQUEST")
  (make-package "MINI::STATUSREQUEST"))
(unless (find-package "MINI::STATUSRESPONSE")
  (make-package "MINI::STATUSRESPONSE"))

(in-package "ROS")





(defclass mini::StatusRequest
  :super ros::object
  :slots (_get_status ))

(defmethod mini::StatusRequest
  (:init
   (&key
    ((:get_status __get_status) 0)
    )
   (send-super :init)
   (setq _get_status (round __get_status))
   self)
  (:get_status
   (&optional __get_status)
   (if __get_status (setq _get_status __get_status)) _get_status)
  (:serialization-length
   ()
   (+
    ;; uint8 _get_status
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _get_status
       (write-byte _get_status s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _get_status
     (setq _get_status (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(defclass mini::StatusResponse
  :super ros::object
  :slots (_status_string ))

(defmethod mini::StatusResponse
  (:init
   (&key
    ((:status_string __status_string) "")
    )
   (send-super :init)
   (setq _status_string (string __status_string))
   self)
  (:status_string
   (&optional __status_string)
   (if __status_string (setq _status_string __status_string)) _status_string)
  (:serialization-length
   ()
   (+
    ;; string _status_string
    4 (length _status_string)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _status_string
       (write-long (length _status_string) s) (princ _status_string s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _status_string
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _status_string (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass mini::Status
  :super ros::object
  :slots ())

(setf (get mini::Status :md5sum-) "b594a92c01db0a8232b059d768ace0a2")
(setf (get mini::Status :datatype-) "mini/Status")
(setf (get mini::Status :request) mini::StatusRequest)
(setf (get mini::Status :response) mini::StatusResponse)

(defmethod mini::StatusRequest
  (:response () (instance mini::StatusResponse :init)))

(setf (get mini::StatusRequest :md5sum-) "b594a92c01db0a8232b059d768ace0a2")
(setf (get mini::StatusRequest :datatype-) "mini/StatusRequest")
(setf (get mini::StatusRequest :definition-)
      "# Possible values for get_status
# uint8 GET_STATUS_VEHICLE_STATE = 0
# uint8 GET_STATUS_CONTROL_MODE = 1
# uint8 GET_STATUS_BATTERY_VOLTAGE = 2
# uint8 GET_STATUS_ERROR_CODE = 3
# uint8 GET_STATUS_MOTION_MODE = 4

# request
uint8 get_status
---
# response
string status_string
")

(setf (get mini::StatusResponse :md5sum-) "b594a92c01db0a8232b059d768ace0a2")
(setf (get mini::StatusResponse :datatype-) "mini/StatusResponse")
(setf (get mini::StatusResponse :definition-)
      "# Possible values for get_status
# uint8 GET_STATUS_VEHICLE_STATE = 0
# uint8 GET_STATUS_CONTROL_MODE = 1
# uint8 GET_STATUS_BATTERY_VOLTAGE = 2
# uint8 GET_STATUS_ERROR_CODE = 3
# uint8 GET_STATUS_MOTION_MODE = 4

# request
uint8 get_status
---
# response
string status_string
")



(provide :mini/Status "b594a92c01db0a8232b059d768ace0a2")


