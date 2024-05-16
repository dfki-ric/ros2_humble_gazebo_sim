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
                                '/world/gz/model/husky/link/base_link/sensor/front_laser/scan@sensor_msgs/msg/LaserScan@ignition.msgs.LaserScan',
				'/world/gz/model/husky/link/base_link/sensor/front_laser/scan/points@sensor_msgs/msg/PointCloud2@ignition.msgs.PointCloudPacked',
				'/world/gz/clock@rosgraph_msgs/msg/Clock@ignition.msgs.Clock'
			],
			remappings=[
				('/model/husky/tf', '/tf'),
				('/model/husky/pose', '/tf'),
				('/world/gz/clock', '/clock')
			],
		),
	])
