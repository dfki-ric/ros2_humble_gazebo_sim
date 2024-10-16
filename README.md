# ros2_ingnition

if ignition gazebo is not installed, you should install the dull desktop for testing here

```
sudo apt install ros-humble-desktop-full
```

# Husky

Please export the variable below so that gazebo finds the husky model

```
export IGN_GAZEBO_RESOURCE_PATH=/path_to/resource:$IGN_GAZEBO_RESOURCE_PATH
```

# Dependencies
```
bash install_dependencies.bash
```

# Usage
```
ros2 launch start.launch.py
```

# References
1) https://app.gazebosim.org/MechaKim2/fuel/worlds/Cave%20Circuit
2) https://app.gazebosim.org/OpenRobotics/fuel/models/COSTAR_HUSKY_SENSOR_CONFIG_1






