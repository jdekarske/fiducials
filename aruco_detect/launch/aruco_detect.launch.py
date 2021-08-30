from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        # Republish any misnamed camera images using /image_transport/republish

        DeclareLaunchArgument('transport', default_value='raw'),
        DeclareLaunchArgument('fiducial_len', default_value='0.14'),
        DeclareLaunchArgument('dictionary', default_value='7'),
        DeclareLaunchArgument('do_pose_estimation', default_value='True'),
        DeclareLaunchArgument('vis_msgs', default_value="False"),
        DeclareLaunchArgument('ignore_fiducials', default_value=""),
        DeclareLaunchArgument('fiducial_len_override', default_value=""),
        Node(
            package='aruco_detect',
            namespace='aruco_detect',
            executable='aruco_detect',
            name='aruco_detect',
            parameters=[
                {"image_transport":LaunchConfiguration('transport')},
                {"publish_images":True},
                {"fiducial_len":LaunchConfiguration('fiducial_len')},
                {"dictionary":LaunchConfiguration('dictionary')},
                {"do_pose_estimation":LaunchConfiguration('do_pose_estimation')},
                {"vis_msgs":LaunchConfiguration('vis_msgs')},
                {"ignore_fiducials":LaunchConfiguration('ignore_fiducials')},
                {"fiducial_len_override":LaunchConfiguration('fiducial_len_override')}
            ],
        )
    ])
