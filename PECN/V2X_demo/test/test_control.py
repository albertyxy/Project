#!/usr/bin/env python

import glob
import os
import sys
import random
import time

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla


def main():
    actor_list = []
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(5.0)
        world = client.get_world()
        blueprint_library = world.get_blueprint_library()
        bp = random.choice(blueprint_library.filter('vehicle.lincoln.mkz_2017'))
        bp.set_attribute('role_name', "scenario")
        transform = carla.Transform(carla.Location(110.0,248.5,0.5),carla.Rotation(0,212,0))
        other_vehicle = world.spawn_actor(bp, transform)
        actor_list.append(other_vehicle)
        other_vehicle.set_autopilot(True)
        time.sleep(10)
        other_vehicle.set_autopilot(False)

        control_vehicle = carla.VehicleControl(throttle=1.0, steer=-0.1)
        other_vehicle.apply_control(control_vehicle)
        time.sleep(3)

        control_vehicle = carla.VehicleControl(throttle=1.0, steer=0.1)
        other_vehicle.apply_control(control_vehicle)
        time.sleep(0.5)

        other_vehicle.set_autopilot(True)
        time.sleep(3)

        other_vehicle.set_autopilot(False)
        control_vehicle = carla.VehicleControl(throttle=1.0, steer=0)
        other_vehicle.apply_control(control_vehicle)
        time.sleep(5)

        other_vehicle.set_autopilot(True)

        time.sleep(50)
    
    finally:
        #client.apply_batch([carla.command.DestroyActor(x) for x in actor_list])
        for actor in actor_list:
            actor.destroy()
        print('destroying actors done')
        

if __name__ == '__main__':
    
    main()
                           