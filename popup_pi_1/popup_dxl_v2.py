#!/usr/bin/env python
#-*-coding: utf-8-*-

import json
import rospy
from std_msgs.msg import String

import dxl

# class 설명
# dxl.bringup(dxl_id) : 다이나믹셀 구동 위한 bringup class .. ex) dxl.bringup(1) = ID:1 인 다이나믹셀 구동 준비
# dxl.setting(dxl_id, velocity, acceleration) : 다이나믹셀 구동 회전 속도, 가속도 설정 .. ex) dxl.bringup(1, 50, 20) = ID:1 인 다이나믹셀 속도 50, 가속도 20으로 설정
# dxl.goal(dxl_id, goal_psition) : 다이나믹셀에 목표 위치 명령 .. ex) dxl.goal(1, 3000) = ID:1 인 다이나믹셀을 위치값 3000인 위치로 회전
# dxl.stop(dxl_id) : 다이나믹셀 구동 중지 .. ex) dxl.stop(1) = ID:1 인 다이나믹셀 구동 중지
# dxl.read(dxl_id).call() : 다이나믹셀 현재 위치값 읽어오기 .. ex) dxl.read(1).call() = ID:1 인 다이나믹셀 현재 위치값 읽어오기

# dxl1, dxl2 = sidetable
dxl.bringup(1)
dxl.setting(1, 80, 20)
dxl.bringup(2)
dxl.setting(2, 80, 20)
# dxl3, dxl4 = bed
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
    bed_mode = strings[0]
    sidetable_mode = strings[1]
    
    if bed_mode == 'b0':
        dxl.goal(3, init_dxl3-16000)
        dxl.goal(4, init_dxl4+16000)
    elif bed_mode == 'b0.5':
        dxl.goal(3, init_dxl3-8000)
        dxl.goal(4, init_dxl4+8000)
    elif bed_mode == 'b1':
        dxl.goal(3, init_dxl3)
        dxl.goal(4, init_dxl4)
    if sidetable_mode == '0':
        dxl.goal(1, init_dxl1+7000)
        dxl.goal(2, init_dxl2-7000)
    elif sidetable_mode == '1':
        dxl.goal(1, init_dxl1)
        dxl.goal(2, init_dxl2)

if __name__ == '__main__':
    listener()
