#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
  pub = rospy.Publisher('limo_status/vehicle_state', String, queue_size = 10)
  pub = rospy.Publisher('limo_status/control_mode', String, queue_size = 10)
  pub = rospy.Publisher('limo_status/vehicle_state', String, queue_size = 10)
  rospy.spin()

if __name__ == '__main__':
  callback(data)