#!/bin/bash
{
	gnome-terminal -- bash -c "bash ~/CARLA_0.9.12/CarlaUE4.sh" 
}&
sleep 5s
{
	gnome-terminal -- bash -c "source ~/carla-ros-bridge/catkin_ws/devel/setup.bash;
	roslaunch carla_ros_bridge carla_ros_bridge.launch" 
}&
sleep 5s
{
	gnome-terminal -- bash -c "python ~/CARLA_0.9.12/PythonAPI/util/config.py --map DripLakev8"
}&
sleep 5s
{
	gnome-terminal -- bash -c "docker run -it --network="host" -e CARLAVIZ_BACKEND_HOST=localhost -e CARLA_SERVER_HOST=localhost -e CARLA_SERVER_PORT=2000 mjxu96/carlaviz:0.9.12"
}