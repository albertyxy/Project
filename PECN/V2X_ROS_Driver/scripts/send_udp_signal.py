#!/usr/bin/env python
import rospy
import json
from v2x_ros_driver.msg import FB_05_Msg, ESP_21_Msg, SARA_06_Msg
import socket

dict_var={}
host = '192.168.2.116'
port = 6801
dest_addr = (host, port)


def callback_1(data):
    global dict_var
    dict_var["Latitude"] = data.FB_Kopfposition_X
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.FB_Kopfposition_X)
    dict_var["Longitude"] = data.FB_Kopfposition_Y
    dict_var["Elevation"] = data.FB_Kopfposition_Z
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = json.dumps(dict_var)
    udp_socket.sendto(msg.encode('utf-8'), dest_addr)
    udp_socket.close()
def callback_2(data):
    global dict_var
    dict_var["Speed"] = data.ESP_v_Signal 
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = json.dumps(dict_var)
    udp_socket.sendto(msg.encode('utf-8'), dest_addr)
    udp_socket.close()   
def callback_3(data):
    global dict_var
    dict_var["LongitudalAcceleration"] = data.SARA_Accel_Y_010
    dict_var["LateralAcceleration"] = data.SARA_Accel_X_010
    dict_var["YawRate"] = data.SARA_Omega_Z_010
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = json.dumps(dict_var)
    udp_socket.sendto(msg.encode('utf-8'), dest_addr)
    udp_socket.close()



def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("sensor_stack/flexray/sc_gw/FB_05", FB_05_Msg, callback_1)
    rospy.Subscriber("sensor_stack/flexray/sc_gw/ESP_21", ESP_21_Msg, callback_2)
    rospy.Subscriber("sensor_stack/flexray/sc_gw/SARA_06", SARA_06_Msg, callback_3)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
