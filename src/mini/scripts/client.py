#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from ..srv import *

req_val = 4

def req(req_val):
    rospy.wait_for_service('Status')
    try:
        get_status = rospy.ServiceProxy('Status', get_status)
        status = get_status(req_val)
        
    except:
      return

def callback(data):
  pub = rospy.Publisher('limo_status/vehicle_state', String, queue_size = 10)
  pub = rospy.Publisher('limo_status/control_mode', String, queue_size = 10)
  pub = rospy.Publisher('limo_status/vehicle_state', String, queue_size = 10)
  pub = rospy.Publisher('/limo_status/error_code', String, queue_size = 10)
  pub = rospy.Publisher('/limo_status/motion_mode', String, queue_size = 10)
  rospy.spin()

if __name__ == '__main__':
  req()
