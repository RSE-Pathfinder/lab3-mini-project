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

limostatusbuff = [0, 0, 0.0, 0, 0]

def callback(data):
    global limostatusbuff
    rospy.loginfo(rospy.get_caller_id() + 'I heard %d', data)
    limostatusbuff[0] = data.vehicle_state
    limostatusbuff[1] = data.control_mode
    limostatusbuff[2] = data.battery_voltage
    limostatusbuff[3] = data.error_code
    limostatusbuff[4] = data.motion_mode

    #IFDEBUG
    print("Translating Status.")
    #ENDIF

def handle_status(req):
    global limostatusbuff
    myStatus = ""
    if req.get_status == 0:
        myStatus = "GET_STATUS_VEHICLE_STATE %s" % limostatusbuff[0]
    elif req.get_status == 1:
        myStatus = "GET_STATUS_CONTROL_MODE %s" % limostatusbuff[1]
    elif req.get_status == 2:
        myStatus = "GET_STATUS_BATTERY_VOLTAGE %s" % limostatusbuff[2]
    elif req.get_status == 3:
        myStatus = "GET_STATUS_ERROR_CODE %s" % limostatusbuff[3]
    elif req.get_status == 4:
        myStatus = "GET_STATUS_MOTION_MODE %s" % limostatusbuff[4]

    #IFDEBUG
    print("Returning Status.")
    #ENDIF

    return myStatus

def status_server():
    rospy.init_node('limo_status_translator_node', anonymous = True)
    rospy.Subscriber('/limo_status', LimoStatus, callback)
    s = rospy.Service('Status', Status, handle_status)

    #IFDEBUG
    print("This is server.") 
    #ENDIF

    rospy.spin()

if __name__ == '__main__':
    try:
        status_server()
    except rospy.ROSInterruptException:
        pass