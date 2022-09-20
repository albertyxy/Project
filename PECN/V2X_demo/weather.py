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
import random
import time  


def main():
    actor_list = []
    try:
        client = carla.Client('127.0.0.1', 2000)
        client.set_timeout(5.0)
        world = client.get_world()
        time.sleep(1)
        weather = carla.WeatherParameters(
        cloudiness=80.0,
        precipitation=30.0,
        sun_altitude_angle=70.0,
        fog_density=100,
        fog_distance=5)
        world.set_weather(weather)
        #print(world.get_weather())


        # blueprint_library = world.get_blueprint_library()
        # bp = random.choice(blueprint_library.filter('vehicle.lincoln.mkz_2017'))
        # bp.set_attribute('role_name', "hero")
        # transform = random.choice(world.get_map().get_spawn_points())
        # vehicle = world.spawn_actor(bp, transform)
        # vehicle.set_autopilot(True)
        # actor_list.append(vehicle)
        # time.sleep(500)

        # set sync mode
        # settings = world.get_settings()
        # settings.synchronous_mode = True
        # settings.fixed_delta_seconds = 0.025
        # world.apply_settings(settings)

        # manually control
        # control = ego_vehicle.get_control()
        # control.throttle = 1.0
        # control.brake = 0.0
        # ego_vehicle.apply_control(control)

    finally:
        #print('destroying actors')
        #camera.destroy()
        #client.apply_batch([carla.command.DestroyActor(x) for x in actor_list])
        print('done.')       
        

if __name__ == '__main__':
    
    main()
    
