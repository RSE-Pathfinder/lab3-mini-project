#!/usr/bin/env python

#IFDEBUG
from __future__ import print_function
#ENDIF

import rospy

from std_msgs.msg import String
##  String data type

from mini.srv import Status
##  Status.srv
#   #request arguement
#   uint8 get_status
#   ---
#   #response
#   string status_string
##  END

# Node
def req():
  # Initialise Node
  rospy.init_node('limo_status_client_node')

  # Initialise Variables
  limo_status = ""
  size = 30
  req_val = 0

  # Waits for active Status service
  print("Waiting for service")
  rospy.wait_for_service('Status')
  rate = rospy.Rate(1)

  # Prevents python from exiting until Node is stopped
  while not rospy.is_shutdown():

    # Send service request
    print("Requesting service")
    get = rospy.ServiceProxy('Status', Status)
    limo_status = get(req_val)

    #IFDEBUG
    print(limo_status.status_string)
    #ENDIF

    # GET_STATUS_VEHICLE_STATE
    if req_val == 0:
      pub0 = rospy.Publisher('/limo_status/vehicle_state', String, queue_size = size)
      pub0.publish(limo_status.status_string)

    # GET_STATUS_CONTROL_MODE
    elif req_val == 1:
      pub1 = rospy.Publisher('/limo_status/control_mode', String, queue_size = size)
      pub1.publish(limo_status.status_string)

    # GET_STATUS_BATTERY_VOLTAGE
    elif req_val == 2:
      pub2 = rospy.Publisher('/limo_status/battery_voltage', String, queue_size = size)
      pub2.publish(limo_status.status_string)

    # GET_STATUS_ERROR_CODE
    elif req_val == 3:
      pub3 = rospy.Publisher('/limo_status/error_code', String, queue_size = size)
      pub3.publish(limo_status.status_string)

    # GET_STATUS_MOTION_MODE
    elif req_val == 4:
      pub4 = rospy.Publisher('/limo_status/motion_mode', String, queue_size = size)
      pub4.publish(limo_status.status_string)
    
    # Cycle Prompt from 0 to 4
    req_val+=1
    if req_val > 4:
      req_val = 0

    rate.sleep()

# Main
if __name__ == '__main__':
  req()
