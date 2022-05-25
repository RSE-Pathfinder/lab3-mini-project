#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

from errno import errorcode
from pickletools import uint8, uint16, float64
import rospy
from std_msgs.msg import String

vehicle_state = 0
control_mode = 0
battery = 0.0
#error_code is an array
error_code = 0
motion_mode = 0

def callback0(data):
    global vehicle_state
    rospy.loginfo(rospy.get_caller_id() + 'I heard %d', data.vs)
    vehicle_state = uint8(data.vs)

def callback1(data):
    global control_mode
    rospy.loginfo(rospy.get_caller_id() + 'I heard %d', data.cm)
    control_mode = uint8(data.cm)

def callback2(data):
    global battery
    rospy.loginfo(rospy.get_caller_id() + 'I heard %d', data.b)
    battery = float64(data.b)

def callback3(data):
    global error_code
    rospy.loginfo(rospy.get_caller_id() + 'I heard %d', data.er)
    error_code = uint16(data.er)
    

def callback4(data):
    global motion_mode
    rospy.loginfo(rospy.get_caller_id() + 'I heard %d', data.mm)
    motion_mode = uint8(data.mm)

def limo_translator_node():
    rospy.init_node('limo_translator_node', anonymous=True)
    rospy.Subscriber('/limo_status/vehicle_state', uint8, callback0)
    rospy.Subscriber('/limo_status/control_mode', uint8, callback1)
    rospy.Subscriber('/limo_status/battery_voltage', float64, callback2)
    rospy.Subscriber('/limo_status/error_code', uint16, callback3)
    rospy.Subscriber('/limo_status/motion_mode', uint8, callback4)
    rospy.spin()

if __name__ == '__main__':
    limo_translator_node()