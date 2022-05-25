#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from .srv import *

def req():
    rospy.wait_for_service('Status')
    try:
        val = rospy.ServiceProxy('Status', Status)

def callback(data):
  pub = rospy.Publisher('limo_status/vehicle_state', String, queue_size = 10)
  pub = rospy.Publisher('limo_status/control_mode', String, queue_size = 10)
  pub = rospy.Publisher('limo_status/vehicle_state', String, queue_size = 10)
  pub = rospy.Publisher('/limo_status/error_code', String, queue_size = 10)
  pub = rospy.Publisher('/limo_status/motion_mode', String, queue_size = 10)
  rospy.spin()

if __name__ == '__main__':
  req()
