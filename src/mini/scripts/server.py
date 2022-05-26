#!/usr/bin/env python

#IFDEBUG
from __future__ import print_function 
#ENDIF

import rospy
from std_msgs.msg import String
##  String data type

from limo_base.msg import LimoStatus
##  LimoStatus.msg
#   Header header
#
#   uint8 vehicle_state
#   uint8 control_mode
#   float64 battery_voltage
#   uint16 error_code
#   uint8 motion_mode
##  END

from mini.srv import Status
##  Status.srv
#   #request arguement
#   uint8 get_status
#   ---
#   #response
#   string status_string
##  END

# Global variable to store LimoStatus
limostatusbuff = [0, 0, 0.0, 0, 0]

# Subscriber
def callback(data):
    global limostatusbuff
    limostatusbuff[0] = data.vehicle_state
    limostatusbuff[1] = data.control_mode
    limostatusbuff[2] = data.battery_voltage
    limostatusbuff[3] = data.error_code
    limostatusbuff[4] = data.motion_mode

    #IFDEBUG
    print("Translating Status.")
    #ENDIF

# Service
def handle_status(req):

    #IFDEBUG
    print("get_status:", req.get_status)
    #ENDIF

    global limostatusbuff
    myStatus = ""
    if req.get_status == 0:
        if limostatusbuff[0] == 0x00:
            myStatus = "GET_STATUS_VEHICLE_STATE: System Normal"
        elif limostatusbuff[0] == 0x02:
            myStatus = "GET_STATUS_VEHICLE_STATE: System Exception"
    elif req.get_status == 1:
        if limostatusbuff[1] == 0x00:
            myStatus = "GET_STATUS_CONTROL_MODE: Standby"
        elif limostatusbuff[1] == 0x01:
            myStatus = "GET_STATUS_CONTROL_MODE: Command Control"
        elif limostatusbuff[1] == 0x02:
            myStatus = "GET_STATUS_CONTROL_MODE: App Control"
        elif limostatusbuff[1] == 0x03:
            myStatus = "GET_STATUS_CONTROL_MODE: Remote Control"
    elif req.get_status == 2:
        myStatus = "GET_STATUS_BATTERY_VOLTAGE: %sV" % limostatusbuff[2]
    elif req.get_status == 3:
        if limostatusbuff[3] > 0x00:
            myStatus = "GET_STATUS_ERROR_CODE: fault"
        else:
            myStatus = "GET_STATUS_ERROR_CODE: no fault"
    elif req.get_status == 4:
        if limostatusbuff[4] == 0x00:
            myStatus = "GET_STATUS_MOTION_MODE: 4-wheel differential"
        elif limostatusbuff[4] == 0x01:
            myStatus = "GET_STATUS_MOTION_MODE: Ackermann"
        elif limostatusbuff[4] == 0x02:
            myStatus = "GET_STATUS_MOTION_MODE: Mecanum"

    #IFDEBUG
    print("Returning Status.")
    #ENDIF

    return myStatus

# Initialise Node
def status_server():
    rospy.init_node('limo_status_translator_node')
    rospy.Subscriber('/limo_status', LimoStatus, callback)
    s = rospy.Service('Status', Status, handle_status)

    #IFDEBUG
    print("This is server.")
    #ENDIF

    rospy.spin()

# Main
if __name__ == '__main__':
    try:
        status_server()
    except rospy.ROSInterruptException:
        pass