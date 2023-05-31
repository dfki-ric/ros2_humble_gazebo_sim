from os import environ

from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable

def generate_launch_description():
	return LaunchDescription([
		SetEnvironmentVariable(name = "IGN_GAZEBO_RESOURCE_PATH", value = "/home/dfki.uni-bremen.de/skasperski/Robotics/models"),
		SetEnvironmentVariable(name = "IGN_GAZEBO_SYSTEM_PLUGIN_PATH", value = ""),
		ExecuteProcess(
			cmd=['ign gazebo empty.sdf -r --force-version 5'],
			output='screen',
			shell=True
		)
	])

