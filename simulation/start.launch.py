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

def load_yaml_file(yaml_file_path):
    try:
        with open(yaml_file_path, 'r') as file:
            return yaml.load(file)
    except EnvironmentError as e: 
        print(str(e))
        return None    

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
  
  if(IfCondition(LaunchConfiguration('use_joystick')).evaluate(context)):

    joy_config_file = str(LaunchConfiguration('joy_config_file').perform(context))
    if joy_config_file == "joy_config_file":
      raise ValueError("Please set the joy_config_file when use_joystick is set to True!")

    joy_config = load_yaml_file(joy_config_file)['joy']['ros__parameters'] 

    joy_node = Node(
      package='joy',
      executable='joy_node',
      name='joy',
      output='both',
      parameters=[joy_config] 
    )

    teleop_twist_config_file = str(LaunchConfiguration('teleop_twist_config_file').perform(context))
    if teleop_twist_config_file == "teleop_twist_config_file":
      raise ValueError("Please set the teleop_twist_config_file when use_joystick is set to True!")

    teleop_twist_config = load_yaml_file(teleop_twist_config_file)

    cmd_vel_topic_name = '/'+robot_name+'/cmd_vel'
    teleop_twist_joy = Node(
    package='teleop_twist_joy',
    executable='teleop_node',
    remappings=[('/cmd_vel', cmd_vel_topic_name)],
    parameters=[teleop_twist_config]
    )

    return [gazebo_launch_description, ign_ros2_bridge_description, joy_node, teleop_twist_joy]   

  return [gazebo_launch_description, ign_ros2_bridge_description]   
  
def generate_launch_description(): 
       
  return LaunchDescription([

    DeclareLaunchArgument(
        "robot_name",
        default_value="husky",
        description="Options: husky"
    ),
        
    DeclareLaunchArgument(
        "world_file_name",
        default_value="cave_circuit",
        description="Options: cave_circuit, urban_circuit_practice_03"
    ),
        
    DeclareLaunchArgument(
        "use_joystick",
        default_value="False",
        description="Use a real joystick."
    ),

    DeclareLaunchArgument(
        "joy_config_file",
        default_value="joy_config_file",
        description="Full path to the joy config"
    ),

    DeclareLaunchArgument(
        "teleop_twist_config_file",
        default_value="teleop_twist_config_file",
        description="Full path to the teleop twist joy config"
    ),

    OpaqueFunction(function = launch_setup)
    
    ])
  