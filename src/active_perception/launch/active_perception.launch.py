"""Launch the full active perception pipeline.

Run from the workspace root (so 'yolov8n.pt' and '.env' resolve):
    ros2 launch active_perception active_perception.launch.py

Then, in a second terminal, start the keyboard control:
    ros2 run active_perception interactive_trigger
(or pass launch_trigger:=true trigger_prefix:='xterm -e' to open it automatically)
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    camera_topic = LaunchConfiguration('camera_topic')
    target_object = LaunchConfiguration('target_object')
    model_path = LaunchConfiguration('model_path')
    gemini_model = LaunchConfiguration('gemini_model')
    env_file = LaunchConfiguration('env_file')
    min_sharpness = LaunchConfiguration('min_sharpness')
    min_illumination = LaunchConfiguration('min_illumination')
    use_webcam = LaunchConfiguration('use_webcam')
    launch_trigger = LaunchConfiguration('launch_trigger')
    trigger_prefix = LaunchConfiguration('trigger_prefix')

    args = [
        DeclareLaunchArgument('camera_topic', default_value='/pi_camera/image_raw',
                              description='Image topic to evaluate (the robot camera)'),
        DeclareLaunchArgument('target_object', default_value='vase',
                              description='COCO class name YOLO looks for, also given to the VLM'),
        DeclareLaunchArgument('model_path', default_value='yolov8n.pt',
                              description='YOLO weights (relative to the launch directory)'),
        DeclareLaunchArgument('gemini_model', default_value='gemini-3.6-flash',
                              description='Gemini model ID used by the VLM bridge'),
        DeclareLaunchArgument('env_file', default_value='.env',
                              description='File holding GEMINI_API_KEY if it is not exported'),
        DeclareLaunchArgument('min_sharpness', default_value='50.0',
                              description='Minimum Laplacian variance of the target ROI'),
        DeclareLaunchArgument('min_illumination', default_value='30.0',
                              description='Minimum mean HSV value (0-255) of the target ROI'),
        DeclareLaunchArgument('use_webcam', default_value='false',
                              description='Publish a local webcam on camera_topic (testing without the robot)'),
        DeclareLaunchArgument('launch_trigger', default_value='false',
                              description='Also start interactive_trigger (needs trigger_prefix terminal)'),
        DeclareLaunchArgument('trigger_prefix', default_value='xterm -e',
                              description='Terminal command used to open interactive_trigger'),
    ]

    nodes = [
        Node(
            package='active_perception',
            executable='live_camera',
            name='live_camera_node',
            output='screen',
            parameters=[{'camera_topic': camera_topic}],
            condition=IfCondition(use_webcam),
        ),
        Node(
            package='active_perception',
            executable='yolo_detector',
            name='yolo_detector_node',
            output='screen',
            parameters=[{'model_path': model_path, 'target_class': target_object}],
        ),
        Node(
            package='active_perception',
            executable='heuristic_scorer',
            name='heuristic_scorer_node',
            output='screen',
        ),
        Node(
            package='active_perception',
            executable='vlm_bridge',
            name='vlm_bridge_node',
            output='screen',
            parameters=[{'model': gemini_model, 'env_file': env_file}],
        ),
        Node(
            package='active_perception',
            executable='coordinator',
            name='coordinator_node',
            output='screen',
            parameters=[{
                'camera_topic': camera_topic,
                'target_object': target_object,
                'min_sharpness': min_sharpness,
                'min_illumination': min_illumination,
            }],
        ),
        Node(
            package='active_perception',
            executable='interactive_trigger',
            name='interactive_trigger',
            prefix=trigger_prefix,
            output='screen',
            condition=IfCondition(launch_trigger),
        ),
        LogInfo(
            msg='Pipeline up. In another terminal run: ros2 run active_perception interactive_trigger',
            condition=UnlessCondition(launch_trigger),
        ),
    ]

    return LaunchDescription(args + nodes)
