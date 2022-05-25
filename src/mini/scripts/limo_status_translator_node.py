#!/usr/bin/env python

#IFDEBUG
from __future__ import print_function 
#ENDIF

import rospy
from std_msgs.msg import String
from limo_base import LimoStatus
from mini.srv import Status
import numpy as np

vehicle_state = 0
control_mode = 0
battery = 0.0
#error_code is an array
error_code = 0
motion_mode = 0

def callback(data):
    global vehicle_state
    rospy.loginfo(rospy.get_caller_id() + 'I heard %d', data.vs)
    vehicle_state = np.uint8(data.vs)
    LimoStatus.vehicle_state

def handle_status(req):
    myStatus = ""
    if req.get_status == 0:
        myStatus = "GET_STATUS_VEHICLE_STATE"
    elif req.get_status == 1:
        myStatus = "GET_STATUS_CONTROL_MODE"
    elif req.get_status == 2:
        myStatus = "GET_STATUS_BATTERY_VOLTAGE"
    elif req.get_status == 3:
        myStatus = "GET_STATUS_ERROR_CODE"
    elif req.get_status == 4:
        myStatus = "GET_STATUS_MOTION_MODE"

    #IFDEBUG
    print("Returning Status.")
    #ENDIF

    return myStatus

def status_server():
    rospy.init_node('status_server', anonymous = True)
    rospy.Subscriber('/limo_status', uint8, callback)
    s = rospy.Service('Status', Status, handle_status)

    #IFDEBUG
    print("This is server.") 
    #ENDIF

    rospy.spin()

if __name__ == '__main__':
    limo_translator_node()
    status_server()