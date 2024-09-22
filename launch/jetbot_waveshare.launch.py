#
# Launch waveshare JetBot motor controller and camera nodes.
#

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node


def generate_launch_description():
    
    # Declare launch arguments
    rtp_output = DeclareLaunchArgument(
        'rtp_output', 
        default_value="DUSTINF-LT1.fios-router.home:1234"
    )

    # Define the motor controller node
    motor_controller = Node(
        package='jetbot_ros',
        executable='motors_waveshare',  # Updated to 'executable' for ROS Humble
        output='screen', 
        emulate_tty=True
    )  
    
    # Return the launch description
    return LaunchDescription([
        rtp_output,
        motor_controller,
    ])
