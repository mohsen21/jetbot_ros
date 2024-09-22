#
# Launch waveshare JetBot motor controller and camera nodes.
#

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    
   
    
    motor_controller = Node(package='jetbot_ros', node_executable='motors_waveshare',
                            output='screen', emulate_tty=True)  
    
    rtp_output = DeclareLaunchArgument('rtp_output', default_value="DUSTINF-LT1.fios-router.home:1234")
    

                        
    return LaunchDescription([
        motor_controller,
        rtp_output,
    ])
