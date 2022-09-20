#!/usr/bin/env python

import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla
import time
import math


import rospy
from std_msgs.msg import UInt8
from V2X_Integration.msg import FB_05_Msg, ESP_21_Msg, SARA_06_Msg, V2X_Warning

x_remote = 0
y_remote = 0
x_host = 0
y_host = 0
distance = 0
speed_remote = 0
speed_host = 0
relative_speed = 0
acceleration_remote = 0
is_same_lane = 0
is_next_lane = 0
warning = 0

def callback_1(data):
    global x_remote
    x_remote = data.FB_Kopfposition_X
    global y_remote
    y_remote = data.FB_Kopfposition_Y

def callback_1_(data):
    global x_host
    x_host= data.FB_Kopfposition_X
    global y_host
    y_host = data.FB_Kopfposition_Y
    global yaw_host
    yaw_host = data.FB_Kopfrotation_Gier
    if yaw_host < 0:
        yaw_host += 360
    global x_remote
    global y_remote
    global distance
    global is_same_lane
    global is_next_lane
    distance = math.sqrt((x_remote-x_host)**2 + (y_remote-y_host)**2)
    angle = math.atan2((y_remote-y_host),(x_remote-x_host))*180/math.pi
    if angle <= 0:
        angle += 360
    diff = abs(angle-yaw_host)
    deviation = distance * math.sin(math.radians(diff))

    if deviation < 3: 
        if is_same_lane == 0:
            is_next_lane = 0
            print("vehicles are on the same lane")
            is_same_lane = 1
    elif deviation >= 3 and deviation < 6:
        if is_next_lane == 0:
            is_same_lane = 0
            print("vehicles are on adjacent lanes")
            is_next_lane = 1
    else:
        is_same_lane = 0
        is_next_lane = 0
    


def callback_2(data):
    global speed_remote
    speed_remote = data.ESP_v_Signal 

def callback_2_(data):
    global speed_host
    speed_host = data.ESP_v_Signal
    global speed_remote
    global relative_speed
    relative_speed = speed_host-speed_remote
 
def callback_3(data):
    global acceleration_remote
    global distance
    global speed_remote
    global relative_speed
    global warning
    acceleration_remote = data.SARA_Accel_Y_010
    warning_msg = V2X_Warning()

    if warning == 11 and (is_same_lane == 0 or distance > 20):
        warning = 10            
        warning_msg.warning_level = 10
        warning_pub.publish(warning_msg)
        print("forward car warning canceled")
        print("distance to host vehicle", distance)
        warning = 0
    elif warning == 21 and (is_next_lane == 0 or distance > 20):
        warning = 20            
        warning_msg.warning_level = 20
        warning_pub.publish(warning_msg)
        print("side car warning canceled")
        print("distance to host vehicle", distance)
        warning = 0
    elif is_same_lane == 1:
        if distance < 20:
            warning = 11
            warning_msg.warning_level = 11
            warning_pub.publish(warning_msg)                
            print("forward car warning")
            print("distance to host vehicle", distance)
            if acceleration_remote < -10 or speed_remote < 1:
                warning_msg.warning_level = 12
                warning_pub.publish(warning_msg)
                print("emergency brake warning")
    elif is_next_lane == 1:
        if distance < 20:
            warning = 21
            warning_msg.warning_level = 21
            warning_pub.publish(warning_msg)
            print("side car warning")
            print("distance to host vehicle", distance)
    


    # #forward car warning 11
    # if is_same_lane == 1 and distance < 20:
    #     if acceleration_remote < -10 or speed_remote < 1:
    #         warning = 11            
    #         warning_msg.warning_level = 1
    #         warning_pub.publish(warning_msg)
    #         print("forward car warning")
    #         print("distance to host vehicle", distance)
    #   #forward car warning canceled 10
    # elif is_same_lane == 1 and distance > 20 and warning == 11:
    #     warning = 10            
    #     warning_msg.warning_level = 0
    #     warning_pub.publish(warning_msg)
    #     print("forward car warning canceled")
    #     print("distance to host vehicle", distance)
    #     warning = 0
    # #side car warning 21
    # elif is_next_lane == 1 and distance < 20:
    #     warning = 21
    #     warning_msg.warning_level = 0
    #     warning_pub.publish(warning_msg)
    #     print("side car warning")
    #     print("distance to host vehicle", distance)
    # #side car warning canceled 20
    # elif is_next_lane == 1 and distance > 20 and warning == 21:
    #     warning_msg.warning_level = 2
    #     warning_pub.publish(warning_msg)
    #     print("side car warning canceled")
    #     print("distance to host vehicle", distance)
    #     warning = 0
    # else:
    #     warning = 0
    #     warning_msg.warning_level = 0
    #     warning_pub.publish(warning_msg)


def listener():
    global x_remote
    global y_remote
    global x_host
    global y_host
    global speed_remote
    global speed_host
    global acceleration_remote

    global warning_pub
    rospy.init_node('safety_function', anonymous=True)
    rospy.Subscriber("/sensor_stack/flexray/sc_gw/FB_05", FB_05_Msg, callback_1)
    rospy.Subscriber("/sensor_stack/flexray/sc_gw/ESP_21", ESP_21_Msg, callback_2)
    rospy.Subscriber("/sensor_stack/flexray/sc_gw/SARA_06", SARA_06_Msg, callback_3)
    rospy.Subscriber("/sensor_stack/flexray/sc_gw/FB_05/host_vehicle", FB_05_Msg, callback_1_)
    rospy.Subscriber("/sensor_stack/flexray/sc_gw/ESP_21/host_vehicle", ESP_21_Msg, callback_2_)
    warning_pub = rospy.Publisher("/forward_car_warning", V2X_Warning, queue_size=10)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
