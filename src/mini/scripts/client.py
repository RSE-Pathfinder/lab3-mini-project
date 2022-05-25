#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    pub = rospy.Publisher('/limo_status/error_code', String, queue_size = 10)
    pub = rospy.Publisher('/limo_status/motion_mode', String, queue_size = 10)
    rospy.spin()