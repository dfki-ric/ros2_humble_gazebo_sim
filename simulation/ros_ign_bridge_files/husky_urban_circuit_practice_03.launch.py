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
				'/model/husky/pose@tf2_msgs/msg/TFMessage@ignition.msgs.Pose_V',
				'/world/urban_circuit_practice_03/model/husky/link/base_link/sensor/front_laser/scan/points@sensor_msgs/msg/PointCloud2@ignition.msgs.PointCloudPacked',
				'/world/urban_circuit_practice_03/clock@rosgraph_msgs/msg/Clock@ignition.msgs.Clock'
			],
			remappings=[
				('/model/husky/cmd_vel', '/husky/cmd_vel'),
				('/model/husky/odometry', '/husky/odometry'),
				('/model/husky/pose', '/tf'),
				('/world/urban_circuit_practice_03/clock', '/clock')
                ('/world/urban_circuit_practice_03/model/husky/link/base_link/sensor/front_laser/scan/points', '/husky/scan/points')

			],
		),
	])
