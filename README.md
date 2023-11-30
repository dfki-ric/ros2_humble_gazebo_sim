# ros2_ingnition

if ignition gazebo is not installed, you should install the dull desktop for testing here

```bash
sudo apt install ros-humble-desktop-full
```

clone this repo to your src folder

```bash
git clone https://git.hb.dfki.de/sw-backbone/examples/ros2_ignition
```

# Husky

Please export the variable below so that gazebo finds the husky model

```export IGN_GAZEBO_RESOURCE_PATH=/opt/workspace/src/ros2_ignition/resource:$IGN_GAZEBO_RESOURCE_PATH```


## start gezebo
cd /opt/workspace/src/ros2_ignition/husky
ign gazebo cave_circuit.sdf --verbose


Launching the first time will take some time for downloading the models.


## start launchfile to bridge topics into ros2
source your install/setup.bash

With ot without Joystick: 


`ros2 launch husky_ros2_bridge_with_joystick.launch.py`

`ros2 launch husky_ros2_bridge_without_joystick.launch.py`

When using without, you can control the robot by starting "Teleop" in gazebo with the "..." menu on the upper right and change the topic in the new ui to /model/husky/cmd_vel.


## using rviz

select the fixedFrame "odom" 

you can also load the husky.rviz configuration from the husky folder.









