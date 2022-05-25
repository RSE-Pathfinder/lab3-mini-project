#!/usr/bin/env python

# uint8 GET_STATUS_VEHICLE_STATE = 0
# uint8 GET_STATUS_CONTROL_MODE = 1
# uint8 GET_STATUS_BATTERY_VOLTAGE = 2
# uint8 GET_STATUS_ERROR_CODE = 3
# uint8 GET_STATUS_MOTION_MODE = 4

# IFDEBUG
from __future__ import print_function
import rospy
from std_msgs.msg import String
from mini.srv import *

def req():
  #Initialise Node
  rospy.init_node('client_node', anonymous=True)
  size = 30
  req_val = 0

  #Waits for active Status service
  print("Waiting for service")
  rospy.wait_for_service('Status')
  rospy.Rate(1)

  #Cycle commands
  req_val+=1
  if req_val > 4:
    req_val = 0

  #Send service request
  print("Requesting service")
  get = rospy.ServiceProxy('Status', Status)
  limo_status = get(req_val)

  rospy.spin()

if __name__ == '__main__':
  req()
