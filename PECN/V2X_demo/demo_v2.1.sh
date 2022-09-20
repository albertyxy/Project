#!/bin/bash
{
	gnome-terminal -- bash -c "python ~/Documents/AlbertYao/V2X_demo/sensors.py"
}&
sleep 2s
{
	gnome-terminal -- bash -c "source ~/carla-ros-bridge/catkin_ws/devel/setup.bash;
	roslaunch carla_spawn_objects carla_spawn_objects.launch objects_definition_file:=/home/carla/Documents/AlbertYao/V2X_demo/objects.json spawn_sensors_only:=True" 
}&
sleep 2s
{
	gnome-terminal -- bash -c "rosrun rviz rviz -d ~/Documents/AlbertYao/V2X_demo/cam+mmv.rviz"
}&

sleep 2s
{
	gnome-terminal -- bash -c "source ~/Documents/AlbertYao/V2X_demo/catkin_ws/devel/setup.bash;
	rosrun V2X_Integration v2x_function.py" 
}&
sleep 2s
{
	gnome-terminal -- bash -c "source ~/Documents/AlbertYao/V2X_demo/catkin_ws/devel/setup.bash;
	rosrun V2X_Integration jupiter_twins.py" 
}&
sleep 2s
{
	gnome-terminal -- bash -c "source ~/Documents/AlbertYao/V2X_demo/catkin_ws/devel/setup.bash;
	rosrun V2X_Integration v2x_signal.py" 
}