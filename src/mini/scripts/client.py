#!/usr/bin/env python

# uint8 GET_STATUS_VEHICLE_STATE = 0
# uint8 GET_STATUS_CONTROL_MODE = 1
# uint8 GET_STATUS_BATTERY_VOLTAGE = 2
# uint8 GET_STATUS_ERROR_CODE = 3
# uint8 GET_STATUS_MOTION_MODE = 4

import rospy
from std_msgs.msg import String
from mini.srv import *

size = 30
req_val = 0

def req():
  #Initialise Node
  rospy.init_node('client_node', anonymous=True)

  #Waits for active Status service
  rospy.wait_for_service('Status')
  rospy.Rate(1)

  try:
      #Cycle commands
      req_val+=1
      if req_val > 4:
        req_val = 0

      #Send service request
      get = rospy.ServiceProxy('Status', Status)
      limo_status = get(req_val)

      #Publish result
      if req_val == 0:
        pub0 = rospy.Publisher('limo_status/vehicle_state', String, queue_size = size)
        pub0.publish(limo_status)
      elif req_val == 1:
        pub1 = rospy.Publisher('limo_status/control_mode', String, queue_size = size)
        pub1.publish(limo_status)
      elif req_val == 2:
        pub2 = rospy.Publisher('limo_status/vehicle_state', String, queue_size = size)
        pub2.publish(limo_status)
      elif req_val == 3:
        pub3 = rospy.Publisher('/limo_status/error_code', String, queue_size = size)
        pub3.publish(limo_status)
      elif req_val == 4:
        pub4 = rospy.Publisher('/limo_status/motion_mode', String, queue_size = size)
        pub4.publish(limo_status)

  except:
      return

  rospy.spin()

if __name__ == '__main__':
  req()
