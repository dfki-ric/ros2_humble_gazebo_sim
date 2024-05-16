# ros2_ingnition

if ignition gazebo is not installed, you should install the dull desktop for testing here

```bash
sudo apt install ros-humble-desktop-full
```

clone this repo to your src folder

```bash
git clone https://git.hb.dfki.de/mos/husky_gz_sim.git
```

# Husky

Please export the variable below so that gazebo finds the husky model

```export IGN_GAZEBO_RESOURCE_PATH=/opt/workspace/src/ros2_ignition/resource:$IGN_GAZEBO_RESOURCE_PATH```


# Usage
ros2 launch start.launch.py








