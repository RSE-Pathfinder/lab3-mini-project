#!/usr/bin/env python

#IFDEBUG
from __future__ import print_function 
#ENDIF

import rospy
from std_msgs.msg import String
from mini.srv import Status

def handle_status(req):
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
    rospy.init_node('status_server')
    s = rospy.Service('Status', Status, handle_status)

    #IFDEBUG
    print("This is server.") 
    #ENDIF

    rospy.spin()
    
if __name__ == "__main__":
    status_server()
