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

# IFDEBUG
from __future__ import print_function
from mini.srv import *
import rospy
from std_msgs.msg import String
from mini.srv import Status

def handle_status(req):
    return {
        '0': Status("GET_STATUS_VEHICLE_STATE"),
        '1': Status("GET_STATUS_CONTROL_MODE"),
        '2': Status("GET_STATUS_BATTERY_VOLTAGE"),
        '3': Status("GET_STATUS_ERROR_CODE"),
        '4': Status("GET_STATUS_MOTION_MODE"),
    } [Status]

def status_server():
    rospy.init_node('status_server')
    s = rospy.Service('Status', Status, handle_status)
    # IFDEBUG
    print("This is server.")
    rospy.spin()
    
if __name__ == "__main__":
    status_server()
