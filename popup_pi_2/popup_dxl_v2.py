#!/usr/bin/env python
#-*-coding: utf-8-*-

import json
import rospy
from std_msgs.msg import String

import dxl

# dxl1, dxl2 = desk
dxl.bringup(1)
dxl.setting(1, 80, 20)
dxl.bringup(2)
dxl.setting(2, 80, 20)
# dxl3, dxl4 = chair
dxl.bringup(3)
dxl.setting(3, 80, 20)
dxl.bringup(4)
dxl.setting(4, 80, 20)

# read init_position of dxl
init_dxl1 = dxl.read(1).call()
init_dxl2 = dxl.read(2).call()
init_dxl3 = dxl.read(3).call()
init_dxl4 = dxl.read(4).call()

def listener():
    rospy.init_node('popup_listener_1', anonymous=True)
    rospy.Subscriber("popup_mode", String, callback)
    rospy.spin()

def callback(data):
    rospy.loginfo(data.data)
    # topic = 'bed:sidetable:chair:desk' ex) '0.5:0:1:1'
    topic = data.data
    # parsing topic ex) '0.5','0','1','1'
    strings = topic.split(':')
    chair_mode = strings[2]
    desk_mode = strings[3]
    if chair_mode == '0':
        dxl.goal(3, init_dxl3-5500)
        dxl.goal(4, init_dxl4-5500)
    elif chair_mode == '1':
        dxl.goal(3, init_dxl3)
        dxl.goal(4, init_dxl4)
    if desk_mode == '0':
        dxl.goal(1, init_dxl1+6800)
        dxl.goal(2, init_dxl2-6800)
    elif desk_mode == '1':
        dxl.goal(1, init_dxl1)
        dxl.goal(2, init_dxl2)

if __name__ == '__main__':
    listener()
    #dxl.goal(1, init_dxl1 - 6800)
    #dxl.goal(2, init_dxl2 + 6800)
    #dxl.goal(3, init_dxl3 + 5500)
    #dxl.goal(4, init_dxl4 + 5500)
