from launch import LaunchDescription
from launch.actions import LogInfo, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    ld = LaunchDescription()
    hello_var = LaunchConfiguration("launch_arg")
    arg_action = DeclareLaunchArgument("launch_arg", default_value="hello launch")

    log_action = LogInfo(msg=hello_var)
    ld.add_action(arg_action)
    ld.add_action(log_action)
    return ld