from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable, ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import EnvironmentVariable, Command, LaunchConfiguration

from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node, SetParameter

def generate_launch_description():


	return LaunchDescription([

		SetParameter(name='use_sim_time', value=True),

		SetEnvironmentVariable(name = "IGN_GAZEBO_RESOURCE_PATH", value = [FindPackageShare('coyote3_description'), "/.."]),
		SetEnvironmentVariable(name = "IGN_GAZEBO_SYSTEM_PLUGIN_PATH", value = EnvironmentVariable("LD_LIBRARY_PATH")),

		ExecuteProcess(
			cmd=["ign gazebo /home/dfki.uni-bremen.de/skasperski/Robotics/ignition/tugbot/tugbot_in_warehouse.sdf -r --force-version 6"],
			output='screen',
			shell=True
		),

		Node(
			package='ros_ign_bridge',
			executable='parameter_bridge',
			arguments=[
				"/model/tugbot/tf@tf2_msgs/msg/TFMessage@ignition.msgs.Pose_V",
				"/model/tugbot/pose@tf2_msgs/msg/TFMessage@ignition.msgs.Pose_V",
				"/model/tugbot/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist",
				"/model/tugbot/odometry@nav_msgs/msg/Odometry@ignition.msgs.Odometry",
				"/world/world_demo/model/tugbot/link/scan_front/sensor/scan_front/scan@sensor_msgs/msg/LaserScan@ignition.msgs.LaserScan",
				
			],
			remappings=[
				("/model/tugbot/tf", "/tf"),
				("/model/tugbot/pose", "/tf"),
				("/model/tugbot/cmd_vel", "/cmd_vel"),
				("/model/tugbot/odometry", "/odom"),
				("/world/world_demo/clock", "/clock")
			]
		),
		
		IncludeLaunchDescription(
			PythonLaunchDescriptionSource([FindPackageShare('slam_toolbox'),'/launch/online_async_launch.py']),
			launch_arguments={
				'slam_params_file': "/home/dfki.uni-bremen.de/skasperski/Robotics/ignition/tugbot/mapper_params_online_async.yaml"
			}.items()
		),
		
		IncludeLaunchDescription(
			PythonLaunchDescriptionSource([FindPackageShare('nav2_bringup'),'/launch/navigation_launch.py']),
			launch_arguments={
				'params_file': "/home/dfki.uni-bremen.de/skasperski/Robotics/ignition/tugbot/nav2_params.yaml"
			}.items()
		)
	])

