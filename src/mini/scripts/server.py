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

# Global Variable to store LimoStatus
limostatusbuff = [0, 0, 0.0, 0, 0]

# Subscriber
def callback(data):

    # Initialise Variables
    global limostatusbuff

    # Assign data from LimoStatus to buffer
    limostatusbuff[0] = data.vehicle_state
    limostatusbuff[1] = data.control_mode
    limostatusbuff[2] = data.battery_voltage
    limostatusbuff[3] = data.error_code
    limostatusbuff[4] = data.motion_mode

# Service
def handle_status(req):

    #IFDEBUG
    print("get_status:", req.get_status)
    #ENDIF

    # Initialise Variables
    global limostatusbuff
    myStatus = ""

    # GET_STATUS_VEHICLE_STATE
    if req.get_status == 0:
        if limostatusbuff[0] == 0x00:
            myStatus = "VEHICLE STATE: System Normal"
        elif limostatusbuff[0] == 0x02:
            myStatus = "VEHICLE STATE: System Exception"

    # GET_STATUS_CONTROL_MODE
    elif req.get_status == 1:
        if limostatusbuff[1] == 0x00:
            myStatus = "CONTROL MODE: Standby"
        elif limostatusbuff[1] == 0x01:
            myStatus = "CONTROL MODE: Command Control"
        elif limostatusbuff[1] == 0x02:
            myStatus = "CONTROL MODE: App Control"
        elif limostatusbuff[1] == 0x03:
            myStatus = "CONTROL MODE: Remote Control"

    # GET_STATUS_BATTERY_VOLTAGE
    elif req.get_status == 2:
        myStatus = "BATTERY VOLTAGE: %sV" % limostatusbuff[2]

    # GET_STATUS_ERROR_CODE
    elif req.get_status == 3:
        if limostatusbuff[3] > 0x00:
            myStatus = "ERROR CODE: fault"
        else:
            myStatus = "ERROR CODE: no fault"

    # GET_STATUS_MOTION_MODE
    elif req.get_status == 4:
        if limostatusbuff[4] == 0x00:
            myStatus = "MOTION MODE: 4-wheel differential"
        elif limostatusbuff[4] == 0x01:
            myStatus = "MOTION MODE: Ackermann"
        elif limostatusbuff[4] == 0x02:
            myStatus = "MOTION MODE: Mecanum"

    # Return
    return myStatus

# Node
def status_server():

    # Node
    rospy.init_node('limo_status_translator_node')

    # Subscriber
    rospy.Subscriber('/limo_status', LimoStatus, callback)

    # Service
    s = rospy.Service('Status', Status, handle_status)

    #IFDEBUG
    print("This is server.")
    #ENDIF

    # Prevents python from exiting until Node is stopped
    rospy.spin()

# Main
if __name__ == '__main__':
    try:
        status_server()
    except rospy.ROSInterruptException:
        pass