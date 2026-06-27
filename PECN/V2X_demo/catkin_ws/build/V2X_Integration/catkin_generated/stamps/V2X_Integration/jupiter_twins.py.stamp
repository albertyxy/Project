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

from V2X_Integration.msg import FB_05_Msg, ESP_21_Msg, SARA_06_Msg

import rospy
#from std_msgs.msg import Header



msg3 = SARA_06_Msg()

def process_imu(imu_data):
    #print("acceleration", imu_data.accelerometer.x)
    global msg3
    msg3.SARA_Accel_Y_010 = imu_data.accelerometer.x


def main():
    #remote info
    msg1 = FB_05_Msg()
    msg2 = ESP_21_Msg()
    global msg3

    #host info
    msg1_ = FB_05_Msg()
    msg2_ = ESP_21_Msg()

    actor_list = []
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(5.0)
        world = client.get_world()
        possible_vehicles = world.get_actors().filter('vehicle.*')
        for vehicle in possible_vehicles:
            if vehicle.attributes['role_name'] == "hero":
                ego_vehicle = vehicle
                print("found ego vehicle")
            if vehicle.attributes['role_name'] == "scenario":
                remote_vehicle = vehicle
                print("found remote vehicle")        
        actor_list.append(ego_vehicle)
        actor_list.append(remote_vehicle)

        # set sync mode
        # settings = world.get_settings()
        # settings.synchronous_mode = True
        # settings.fixed_delta_seconds = 0.025
        # world.apply_settings(settings)

        #add an imu sensor to remote vehicle
        bp = world.get_blueprint_library().find('sensor.other.imu')
        imu = world.spawn_actor(bp, carla.Transform(), attach_to = remote_vehicle)
        imu.listen(lambda imu_data:process_imu(imu_data))
        actor_list.append(imu)
        #ros topic setup
        rv_acceleration_pub = rospy.Publisher("/sensor_stack/flexray/sc_gw/SARA_06", SARA_06_Msg, queue_size=100)
        rv_speed_pub = rospy.Publisher("/sensor_stack/flexray/sc_gw/ESP_21", ESP_21_Msg, queue_size=100)
        hv_speed_pub = rospy.Publisher("/sensor_stack/flexray/sc_gw/ESP_21/host_vehicle", ESP_21_Msg, queue_size=100)
        rv_position_pub = rospy.Publisher("/sensor_stack/flexray/sc_gw/FB_05", FB_05_Msg, queue_size=100)
        hv_position_pub = rospy.Publisher("/sensor_stack/flexray/sc_gw/FB_05/host_vehicle", FB_05_Msg, queue_size=100)
        rospy.init_node('jupiter', anonymous=True)
        rate = rospy.Rate(2) # 10hz
        while not rospy.is_shutdown():
            rv_acceleration_pub.publish(msg3)
            v = remote_vehicle.get_velocity()
            speed = 3.6 * math.sqrt(v.x**2 + v.y**2 + v.z**2)
            msg2.ESP_v_Signal = speed
            rv_speed_pub.publish(msg2)
            v_ = ego_vehicle.get_velocity()
            speed_ = 3.6 * math.sqrt(v_.x**2 + v_.y**2 + v_.z**2)
            msg2_.ESP_v_Signal = speed_
            hv_speed_pub.publish(msg2_)
            msg1.FB_Kopfposition_X = remote_vehicle.get_transform().location.x
            msg1_.FB_Kopfposition_X = ego_vehicle.get_transform().location.x
            msg1.FB_Kopfposition_Y = remote_vehicle.get_transform().location.y
            msg1_.FB_Kopfposition_Y = ego_vehicle.get_transform().location.y
            msg1_.FB_Kopfrotation_Gier = ego_vehicle.get_transform().rotation.yaw
            rv_position_pub.publish(msg1)
            hv_position_pub.publish(msg1_)

            rate.sleep()

    finally:
        #client.apply_batch([carla.command.DestroyActor(x) for x in actor_list])
        # for actor in actor_list:
        #     actor.destroy()
        client.apply_batch([carla.command.DestroyActor(x) for x in actor_list])
        print('destroying actors done')

if __name__ == '__main__':
    
    main()


  


