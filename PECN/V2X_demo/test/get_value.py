#!/usr/bin/env python

import glob
import os
import sys
import random
import math
import time

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla
# imu_data = carla.IMUMeasurement() 

ax = 0
def process_imu(imu_data):
    # print("acceletation")
    # print(imu_data.accelerometer.x)
    global ax 
    ax = imu_data.accelerometer.x


def main():
    actor_list = []
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(5.0)
        world = client.get_world()
        # blueprint_library = world.get_blueprint_library()
        # bp = random.choice(blueprint_library.filter('vehicle.lincoln.mkz_2017'))
        # bp.set_attribute('role_name', "hero")
        # transform = random.choice(world.get_map().get_spawn_points())
        # ego_vehicle = world.spawn_actor(bp, transform)
        # actor_list.append(ego_vehicle)
        

        possible_vehicles = world.get_actors().filter('vehicle.*')
        for vehicle in possible_vehicles:
            print(vehicle.attributes)
            if vehicle.attributes['role_name'] == "hero":
                ego_vehicle = vehicle
                print("found")
        actor_list.append(ego_vehicle)
        

        bp = world.get_blueprint_library().find('sensor.other.imu')
        imu = world.spawn_actor(bp, carla.Transform(), attach_to = ego_vehicle)
        imu.listen(lambda imu_data:process_imu(imu_data))
        actor_list.append(imu)
        time.sleep(1)
        # ego_vehicle.set_autopilot(True)

 
        while True:
            t = ego_vehicle.get_transform().location
            print(t)
            v = ego_vehicle.get_velocity()
            speed = 3.6 * math.sqrt(v.x**2 + v.y**2 + v.z**2)
            print("speed:",speed)
            print("accele",ax)
            print("yaw",ego_vehicle.get_transform().rotation.yaw)
            time.sleep(1)
            # print("accele")
            # print(imu_data.accelerometer.x)


        # map = world.get_map()
        # spawn_points = world.get_map().get_spawn_points()
        # random.shuffle(spawn_points)
        # possible_vehicles = world.get_actors().filter('vehicle.*')
        # for vehicle in possible_vehicles:
        #     if vehicle.attributes['role_name'] == "hero":
        #         ego_vehicle = vehicle
        #     else:
        #         print("found ego vehicle")
        # actor_list.append(ego_vehicle)

        # agent = BehaviorAgent(ego_vehicle, behavior='aggressive')
        # current_waypoint = map.get_waypoint(ego_vehicle.get_location())
        # destination = carla.Transform(carla.Location(x=-44.2, y=-127.3, z=0), carla.Rotation(pitch=0.000000, yaw=-120.202332, roll=0.000000))
        # # if spawn_points[0].location != ego_vehicle.get_location():
        # #     destination = spawn_points[0]
        # # else:
        # #     destination = spawn_points[1]        
        # left_waypoint=current_waypoint.get_left_lane()
        # agent.set_destination(left_waypoint.transform.location, destination)
        # while True:
        #     if agent.done():
        #         print("The target has been reached, stopping the simulation")
        #         break
        #     ego_vehicle.apply_control(agent.run_step())

        # while True:
        #     if agent.done():
        #         agent.set_destination(random.choice(spawn_points).location)
        #         print("The target has been reached, searching for another target")

        #     vehicle.apply_control(agent.run_step())
    


    finally:
        #client.apply_batch([carla.command.DestroyActor(x) for x in actor_list])
        for actor in actor_list:
            actor.destroy()
        print('destroying actors done')
        

if __name__ == '__main__':
    
    main()
                           