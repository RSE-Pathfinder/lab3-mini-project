#!/usr/bin/env python

# uint8 GET_STATUS_VEHICLE_STATE = 0
# uint8 GET_STATUS_CONTROL_MODE = 1
# uint8 GET_STATUS_BATTERY_VOLTAGE = 2
# uint8 GET_STATUS_ERROR_CODE = 3
# uint8 GET_STATUS_MOTION_MODE = 4

import rospy
from std_msgs.msg import String
from ..srv import *

size = 30
req_val = 0

def req():
  rospy.wait_for_service('Status')
  rospy.Rate(1)
  try:
      req_val+=1
      if req_val > 4:
        req_val = 0
        
      get_status = rospy.ServiceProxy('Status', get_status)
      status = get_status(req_val)

      if status == "GET_STATUS_VEHICLE_STATE":
        pub0 = rospy.Publisher('limo_status/vehicle_state', String, queue_size = size)
      elif status == "GET_STATUS_CONTROL_MODE":
        pub1 = rospy.Publisher('limo_status/control_mode', String, queue_size = size)
      elif status == "GET_STATUS_BATTERY_VOLTAGE":
        pub2 = rospy.Publisher('limo_status/vehicle_state', String, queue_size = size)
      elif status == "GET_STATUS_ERROR_CODE":
        pub3 = rospy.Publisher('/limo_status/error_code', String, queue_size = size)
      elif status == "GET_STATUS_MOTION_MODE":
        pub4 = rospy.Publisher('/limo_status/motion_mode', String, queue_size = size)

  except:
      return

  rospy.spin()

if __name__ == '__main__':
  req()
