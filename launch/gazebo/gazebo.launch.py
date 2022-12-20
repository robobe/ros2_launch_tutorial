from launch import LaunchDescription
import os
from ament_index_python.packages import get_package_share_directory
from launch.actions import LogInfo, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    gazebo_pkg = get_package_share_directory('gazebo_ros')
    ld = LaunchDescription()
    verbose = LaunchConfiguration("verbose")
    arg_gazebo_verbose = DeclareLaunchArgument("verbose", default_value="true")

    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    gazebo_pkg, 'launch', 'gazebo.launch.py')]),
                    launch_arguments={'verbose': verbose}.items()
             )

    ld.add_action(arg_gazebo_verbose)
    ld.add_action(gazebo)
    return ld