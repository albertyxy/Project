#!/usr/bin/env python
# license removed for brevity
import rospy
import json
import socket
from v2x_ros_driver.msg import BSM


def talker():
    host = ''
    port = 6800
    dest_addr = (host, port)
    msg_to_send=BSM()
    pub = rospy.Publisher('BSM_msg', BSM, queue_size=50)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(dest_addr)
    while not rospy.is_shutdown():
        #receive less than 1024 Byte
        msg, addr = s.recvfrom(1024)
        msg = msg.decode('utf-8')
        f = json.loads(msg)
        if "Id" in f:
            msg_to_send.id=f["Id"]
        if "MsgCount" in f:
            msg_to_send.message_count=f["MsgCount"]        
        if "Latitude" in f:
            msg_to_send.latitude=f["Latitude"]
        if "Longtitude" in f:
            msg_to_send.longtitude=f["Longtitude"]
        if "Elevation" in f:
            msg_to_send.elevation=f["Elevation"]
        if "SemiMajorAxisAccuracy" in f:
            msg_to_send.pos_accuracy_semi_major=f["SemiMajorAxisAccuracy"]
        if "SemiMinorAxisAccuracy" in f:
            msg_to_send.pos_accuracy_semi_minor=f["SemiMinorAxisAccuracy"]
        if "SemiMajorAxisOrientation" in f:
            msg_to_send.pos_accuracy_orientation=f["SemiMajorAxisOrientation"]
        if "LateralAcceleration" in f:
            msg_to_send.lateral_acceleration=f["LateralAcceleration"]
        if "LongitudalAcceleration" in f:
            msg_to_send.longitudinal_acceleration=f["LongitudalAcceleration"]
        if "VerticalAcceleration" in f:
            msg_to_send.vert_acceleration=f["VerticalAcceleration"]
        if "YawRate" in f:
            msg_to_send.yaw_acceleration=f["YawRate"]
        if "TransmissionState" in f:
            msg_to_send.transmission_state=f["TransmissionState"]
        if "ResponseType" in f:
            msg_to_send.response_type=f["ResponseType"]
        if "LightbarInUse" in f:
            msg_to_send.light_use=f["LightbarInUse"]
        if "SirenInUse" in f:
            msg_to_send.siren_use=f["SirenInUse"]
        if "Events" in f:
            msg_to_send.events=f["Events"]
        if "Light" in f:
            msg_to_send.vert_acceleration=f["Light"]
        if "PostionConfidence" in f:
            msg_to_send.confidence_position=f["PostionConfidence"]
        if "ElevationConfidence" in f:
            msg_to_send.confidence_elevation=f["ElevationConfidence"]
        if "BasicVehicleClass" in f:
            msg_to_send.vehicle_class=f["BasicVehicleClass"]
        if "FuelType" in f:
            msg_to_send.vehicle_fuel_type=f["FuelType"]
        if "Heading" in f:
            msg_to_send.heading=f["Heading"]
        if "Speed" in f:
            msg_to_send.speed=f["Speed"]
        if "SteeringWheelAngle" in f:
            msg_to_send.angle=f["SteeringWheelAngle"]
        if "Height" in f:
            msg_to_send.vehicle_height=f["Height"]
        if "Width" in f:
            msg_to_send.vehicle_width=f["Width"]
        if "Length" in f:
            msg_to_send.vehicle_lenth=f["Length"]
        if "BrakePadel" in f:
            msg_to_send.brake_padel=f["BrakePadel"]
        if "WheelBrakes" in f:
            msg_to_send.wheel_brakes=f["WheelBrakes"]
        if "Traction" in f:
            msg_to_send.traction=f["Traction"]
        if "ABS" in f:
            msg_to_send.abs=f["ABS"]
        if "SCS" in f:
            msg_to_send.scs=f["SCS"]
        if "BrakeBoost" in f:
            msg_to_send.brake_boost=f["BrakeBoost"]
        if "AuxBrakes" in f:
            msg_to_send.aux_brakes=f["AuxBrakes"]
       
        rospy.loginfo(msg_to_send)
        pub.publish(msg_to_send)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
