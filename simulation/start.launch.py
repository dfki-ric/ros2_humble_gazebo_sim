import yaml
import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node  
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from launch.actions import OpaqueFunction, DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import Command, FindExecutable, LaunchConfiguration
from launch.conditions import IfCondition  
from launch.launch_description_sources import PythonLaunchDescriptionSource

def launch_setup(context, *args, **kwargs):

  world_file_name = str(LaunchConfiguration('world_file_name').perform(context))
  robot_name = str(LaunchConfiguration('robot_name').perform(context))

  ign_args = ' -r models/'+world_file_name+'.sdf'

  gazebo_launch_description = IncludeLaunchDescription(
	PythonLaunchDescriptionSource(
		os.path.join(
			get_package_share_directory('ros_ign_gazebo'),
			'launch',
			'ign_gazebo.launch.py'
		)
	),
	launch_arguments={
		'ign_args': ign_args,
		'ign_version': '6'
	}.items()
  )

  bridge_launch_file = 'ros_ign_bridge_files/'+robot_name+'_'+world_file_name+'.launch.py'
  ign_ros2_bridge_description = IncludeLaunchDescription(
			PythonLaunchDescriptionSource(bridge_launch_file)
		)

  rviz_node = Node(
	package="rviz2",
	executable="rviz2",
	name="rviz2",
	output="log",
	#arguments=["-d", rviz_config] 
  )

  joy_node = Node(
    package='joy',
    executable='joy_node',
    name='joy',
    output='both',
    #parameters=[joy_config] 
  )

  cmd_vel_topic_name = '/model/'+robot_name+'/cmd_vel'
  teleop_twist_joy = Node(
	package='teleop_twist_joy',
	executable='teleop_node',
	remappings=[('/cmd_vel', cmd_vel_topic_name)],
	parameters=[{
		"require_enable_button": False,
		"axis_linear.x"    : 1,
		"axis_angular.x"   : 0,
		"scale_linear.x"   : 0.5,
		"scale_angular.yaw": 0.5
	}]
	)
  
  if(IfCondition(LaunchConfiguration('use_joystick')).evaluate(context)):
    return [gazebo_launch_description, ign_ros2_bridge_description, joy_node, teleop_twist_joy, rviz_node]   

  return [gazebo_launch_description, ign_ros2_bridge_description, rviz_node]   
  
def generate_launch_description(): 
       
  return LaunchDescription([

    DeclareLaunchArgument(
        "robot_name",
        default_value="husky",
        description="Name of the robot."
    ),
        
    DeclareLaunchArgument(
        "world_file_name",
        default_value="cave_circuit",
        description="Name of the world file."
    ),
        
    DeclareLaunchArgument(
        "use_joystick",
        default_value="false",
        description="Use a real joystick."
    ),

    OpaqueFunction(function = launch_setup)
    
    ])
  