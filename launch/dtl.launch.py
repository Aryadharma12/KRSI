from launch import LaunchDescription
from launch_ros.actions import Node

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    depth_params = os.path.join(get_package_share_directory('krsi'),'config','convert.yaml')

    convert_node = Node(
            package='depthimage_to_laserscan',
            executable='depthimage_to_laserscan_node',
            parameters=[depth_params],
            remappings=[
            ('/image', '/camera/depth/image_raw'),
            ('/camera_info', '/camera/depth/camera_info'),
        ]
         )
    
    return LaunchDescription([
        convert_node,  
    ])