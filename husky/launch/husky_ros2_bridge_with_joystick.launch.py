from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return LaunchDescription([
		Node(
			package='ros_ign_bridge',
			executable='parameter_bridge',
			arguments=[
				'/model/husky/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist',
				'/model/husky/odometry@nav_msgs/msg/Odometry@ignition.msgs.Odometry',
				'/model/husky/tf@tf2_msgs/msg/TFMessage@ignition.msgs.Pose_V',
				'/model/husky/pose@tf2_msgs/msg/TFMessage@ignition.msgs.Pose_V',
				'/world/gz/model/husky/link/base_link/sensor/front_laser/scan/points@sensor_msgs/msg/PointCloud2@ignition.msgs.PointCloudPacked',
				'/world/gz/clock@rosgraph_msgs/msg/Clock@ignition.msgs.Clock"'
			],
			remappings=[
				('/model/husky/tf', '/tf'),
				('/model/husky/pose', '/tf'),
				('/world/gz/clock', '/clock')
			]
		),
		Node(
			package='joy',
			executable='joy_node'
		),
		Node(
			package='teleop_twist_joy',
			executable='teleop_node',
			remappings=[('/cmd_vel', '/model/husky/cmd_vel')],
			parameters=[{
				"require_enable_button": False,
				"axis_linear.x"    : 1,
				"axis_angular.x"   : 0,
				"scale_linear.x"   : 0.5,
				"scale_angular.yaw": 0.5
			}]
		),
	])

