from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from ament_index_python.packages import get_package_share_directory

import os

def generate_launch_description():
	return LaunchDescription([

		# Gazebo
		IncludeLaunchDescription(
			PythonLaunchDescriptionSource(
				os.path.join(
					get_package_share_directory('ros_ign_gazebo'),
					'launch',
					'ign_gazebo.launch.py'
				)
			),
			launch_arguments={
				'ign_args': ' -r models/cave_circuit.sdf',
				'ign_version': '6'
			}.items()
		),

		# IGN-ROS-Bridge
		IncludeLaunchDescription(
			PythonLaunchDescriptionSource('launch/husky_ros2_bridge_without_joystick.launch.py')
		)
	])

