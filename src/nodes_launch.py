from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_pac',
            executable='app',
            name='app'
        ),
        Node(
            package='my_pac',
            executable='s_to_t',
            name='s_to_t'
        ),
        Node(
            package='my_pac',
            executable='t_analysis',
            name='t_analysis'
        )
    ])
