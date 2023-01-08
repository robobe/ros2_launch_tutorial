from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable

def generate_launch_description():
    log_format_env = SetEnvironmentVariable(name="RCUTILS_CONSOLE_OUTPUT_FORMAT", value="[{severity} {time}] [{name} ({line_number})]: {message} ")
    node = Node(name="minimal_node",
        package="pkg_launch_tutorial",
        executable="minimal_node.py",
        arguments=['--ros-args', '--log-level', 'info']
    )
    
    ld = LaunchDescription()
    ld.add_action(log_format_env)
    ld.add_action(node)

    return ld