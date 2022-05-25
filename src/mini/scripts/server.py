#!/usr/bin/env python

## Possible values for get_status
## uint8 GET_STATUS_VEHICLE_STATE = 0
## uint8 GET_STATUS_CONTROL_MODE = 1
## uint8 GET_STATUS_BATTERY_VOLTAGE = 2
## uint8 GET_STATUS_ERROR_CODE = 3
## uint8 GET_STATUS_MOTION_MODE = 4

## request
#uint8 get_status
#---
## response
#string status_string

from mini.srv import get_status,status_string
import rospy
from std_msgs.msg import String

def handle_status(req):
    return {
        '0': status_string("GET_STATUS_VEHICLE_STATE"),
        '1': status_string("GET_STATUS_CONTROL_MODE"),
        '2': status_string("GET_STATUS_BATTERY_VOLTAGE"),
        '3': status_string("GET_STATUS_ERROR_CODE"),
        '4': status_string("GET_STATUS_MOTION_MODE"),
    } [status_string]

def status_server():
    rospy.init_node('status_server')
    s = rospy.Service('status', get_status, handle_status)
    rospy.spin()
    
if __name__ == "__main__":
    status_server()
