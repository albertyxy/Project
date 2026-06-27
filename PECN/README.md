# v2x_Jupiter_Integration



This is the repository of PECN ADAS HiL project from Porsche Engineering Shanghai, and the software stack is based on CARLA Simulator, ROS and V2X OBU(On Board Unit), focusing on the integration of V2X system,  Jupiter Twins and PevaTec Carla. This project aims to realize safety function for scenario test using basic safety message from V2X system, and offer interface between Jupiter Node and V2X OBU which use ROS as the middleware for info transmission.



This repository is maintained by xiangyin.yao@porsche-engineering.cn

Functions available now:

- Forward Car Warning

- Side Car Warning



**Stack Dependencies**

- CARLA Simulator 0.9.12
- Ubuntu 18.04
- ROS melodic desktop
- CARLA-ROS-BRIDGE 0.9.12
- Carla ScenarioRunner 0.9.12
- Roadrunner 2021b
- Houdini
- Unreal Engine 4.26





### Jupiter Twins Node

[Jupiter twins node](./V2X_demo/catkin_ws/src/V2X_Integration/scripts/jupiter_twins.py) can transform the info of host vehicle and remote vehicle in Carla world into Jupiter ROS topic format. In this demo, the Jupiter node can support following message, i.e. position, speed, heading, and acceleration (see in [BSM Signal.xlsx Sheet 2](./BSM Signal.xlsx)). More signals can be implemented in the future development.



### Safety function Node

Safety function Node can subscribe the related ROS topic from Jupiter Node and ROS Driver, and then send a variety of warning signals as a ROS topic (see in [BSM Signal.xlsx Sheet 3](./BSM Signal.xlsx)). Depending on the level value of warning, the ego vehicle can make different decisions. For example, when it receive emergency brake warning signal, it will brake. And it will not change the lane until the side car warning is canceled. The basic logic of warning can be viewed in [v2x_signal.py](./V2X_demo/catkin_ws/src/V2X_Integration/scripts/v2x_signal.py). And the logic to control ego vehicle can be viewed in [v2x_function.py](./V2X_demo/catkin_ws/src/V2X_Integration/scripts/v2x_function.py). All ROS topics in this demo can be found in [rosgraph.png](./V2X_demo/showcase/rosgraph.png)



### V2X_ROS_Driver

v2x_ros_driver is a ROS package for data transmission between v2x system(e.g. OBU) and ROS environment. Till now, only BSM(basic safety message) is done. ["send_udp_signal.py"](./V2X_ROS_Driver/scripts/send_udp_signal.py) Node will firstly subscribe related topics from Jupiter and then send the data to V2X side in JSON format via UDP; ["receive_udp_signal.py"](./V2X_ROS_Driver/scripts/receive_udp_signal.py) Node will firstly receive the data from V2X system via UDP and encode all info as a ROS topic called "BSM_msg". All signals can be viewed in BSM Signal.xlsx.

```bash
#usage(in the ROS Environment)
catkin_make
source devel/setup.bash
roscore
rosrun v2x_ros_driver send_upd_signal.py
rosrun v2x_ros_driver receive_upd_signal.py


#test(outside the ROS Environment)
cd test
python udp_server.py
python udp_client.py
```



### [V2X_ROS_app](./V2X_demo/showcase/OBU_Signal_Test.webm)

v2x_ros_app involves apps running in OBU hardware. 

["v2x_ros_receive"](./V2X_ROS_App/bin/v2x_ros_receive) is used to receive the simulated BSM message sent from ROS and forward it to the wireless transmission module WMS of the OBU. ["v2x_ros_send"](./V2X_ROS_App/bin/v2x_ros_send) is used to send info received from another OBU back to ROS environment. At the same time, some log information will be printed with the help of the v2x_com_log program.

The v2x_wmh wireless transceiver processing module, originally used as a bridge between the WMS and the application layer, is responsible for encoding and decoding the information exchange between two OBUs. In this project, the application layer and WMS communicate directly through transparent transmission(Transparent transmission refers to the direct communication between v2x_ros_* and the WMS module). And WMS is responsible for the encoding and decoding of PC5 communication.

```bash
#compile and configure(in virtual machine)
source /opt/genvict-imx-fb/4.1.15-1.2.1/environment-setup-cortexa9hf-vfp-neon-poky-linux-gnueabi
$CC -g v2x_ros_receive.c cJSON.c -o v2x_ros_receive -I /home/v2x/V2X_Project/V2X_ROS_app/inc
$CC -g v2x_ros_send.c cJSON.c -o v2x_ros_send -I /home/v2x/V2X_Project/V2X_ROS_app/inc
scp ./v2x_ros_receive root@OBU-116:/home/root/v2x_app/
scp ./v2x_ros_send root@OBU-115:/home/root/v2x_app/

#test(in OBU)
cd v2x_app/
./v2x_ros_send
./v2x_ros_receive
```



### Scenario Description

[**demo1(Forward Car Warning)**](./V2X_demo/showcase/demo1.mp4)

In this scenario, there are two cars(one is ego_vehicle, the other is remote_vehicle) in the same lane. The remote vehicle is driving in front of the ego vehicle with a constant speed. When the relative distance is less than 20 m, the remote vehicle will send a forward_car_warning signal to the ego vehicle. When the remote vehicle brakes (near the intersection), it will also send out an emergency brake warning. Once the ego vehicle detect this emergency brake warning signal, it will also brake.

```bash
#run demo1
./env_setup.sh
python3 scenario_runner.py --scenario FCW_demo
./demo_v1.1.sh
```

[**demo2(Side Car Warning)**](./V2X_demo/showcase/demo2.mp4)

In this scenario, there are three cars(one is ego_vehicle, the other two are remote_vehicle). At the beginning ,the ego vehicle will follow the remote vehicle 01 which is a large truck. This large truck drives too slowly so that the ego vehicle need to change the lane and overtake it. However, because of the foggy weather, the ego vehicle doesn't have the view of the lane beside, so it need check the BSM signal from the remote vehicle 02 and then decide if it can change the lane or not. When the distance between vehicle 02 and ego vehicle is less than 20 m,  vehicle 02 will send a side_car_warning signal, hence, the ego vehicle cannot change the lane. Only the side_car_warning signal is canceled,  the ego vehicle can execute a lane-change behavior. 

```bash
#run demo2
./env_setup.sh
python3 scenario_runner.py --scenario SCW_demo
./demo_v2.1.sh
```

demo1 and demo2 is based on the custom map(DripLake). In demo1, a variety of sensors including lidar, radar, rgb camera, semantic camera etc. is attached to the ego vehicle(see in objects.json). In demo2, only a front camera and a millimeter wave radar is configured. All sensor data can be visualized both in Rviz and Carlaviz.(open a browser---localhost:8080)

```bash
#after the simulation, clean the docker image of Carlaviz
docker system prune
```



