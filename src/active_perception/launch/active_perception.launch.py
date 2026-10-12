"""Launch the full active perception pipeline (laptop side).

The robot must already be running its bringup, e.g.
    ros2 launch lyra_bringup robot.launch.py mode:=slam camera:=true imu:=true

Run from the workspace root (so 'yolov8n.pt', '.env' and 'runs/' resolve):
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


# (name, default, description) - every one becomes a launch argument
ARGS = [
    # Perception
    ('camera_topic', '/pi_camera/image_raw/compressed',
     "Camera topic; '/compressed' topics are read as JPEG CompressedImage"),
    ('target_object', 'vase', 'COCO class name YOLO looks for, also given to the VLM'),
    ('model_path', 'yolov8n.pt', 'YOLO weights (relative to the launch directory)'),
    ('gemini_model', 'gemini-3.6-flash', 'Gemini model ID used by the VLM bridge'),
    ('env_file', '.env', 'File holding GEMINI_API_KEY if it is not exported'),
    ('min_sharpness', '50.0', 'Minimum Laplacian variance of the target ROI'),
    ('min_illumination', '30.0', 'Minimum mean HSV value (0-255) of the target ROI'),
    ('runs_dir', 'runs', 'Folder that gets one run_<timestamp> folder per session'),
    # Motion (BeetleBot / Lyra)
    ('enable_motion', 'true', 'Move to the next orbit view before every snapshot but the first'),
    ('orbit_radius', '0.8', 'Distance (m) from the robot centre to the target at the start'),
    ('orbit_step_deg', '30.0', 'Degrees around the target per step'),
    ('orbit_direction', 'ccw', "'ccw' or 'cw' around the target, seen from above"),
    ('linear_speed', '0.15', 'Drive speed (m/s)'),
    ('angular_speed', '0.5', 'Max turn speed (rad/s)'),
    ('min_angular_speed', '0.25', 'Lowest turn speed (rad/s); raise it if the robot stalls near the end of a turn'),
    ('settle_sec', '1.0', 'Wait after stopping before taking the snapshot'),
    ('cmd_vel_topic', '/cmd_vel_nav', 'Velocity command topic on the robot'),
    ('odom_topic', '/odometry/filtered', 'Odometry used for turns/distance (or /wheel/odom)'),
    ('scan_topic', '/scan', 'Lidar used for the obstacle stop'),
    ('obstacle_stop_enabled', 'true', 'Stop driving if the lidar sees something close in front'),
    ('turn_source', 'imu', "Measure turns with 'imu' (gyro) or 'odom' (skid-steer odom over-reports turns)"),
    ('imu_topic', '/imu/data', 'IMU whose gyro z is used for turns'),
    ('imu_yaw_sign', '1.0', 'Set -1.0 if the gyro reads negative for a LEFT turn'),
    ('odom_turn_scale', '1.0', 'odom-reported / real rotation, only for turn_source:=odom'),
    ('imu_gyro_scale', '1.0', 'Gyro multiplier to rad/s: 0.0174533 if the IMU publishes deg/s'),
    ('odom_distance_scale', '1.0', 'odom-reported / real straight-line distance'),
    ('scan_ignore_below', '0.23', 'Ignore lidar readings closer than this (m): the robot itself'),
    ('robot_front_offset', '0.19', 'Lidar centre to front bumper (m)'),
    ('obstacle_clearance', '0.15', 'Stop driving when something is this close to the bumper (m)'),
    ('scan_front_angle_deg', '0.0', 'Lidar angle pointing to the robot front (180 if mounted reversed)'),
    ('use_arming', 'true', 'Call /lyra/arm before and /lyra/disarm after each move'),
    # Testing helpers
    ('use_webcam', 'false', 'Publish a local webcam on camera_topic (testing without the robot)'),
    ('launch_trigger', 'false', 'Also start interactive_trigger (needs trigger_prefix terminal)'),
    ('trigger_prefix', 'xterm -e', 'Terminal command used to open interactive_trigger'),
]


def generate_launch_description():
    c = {name: LaunchConfiguration(name) for name, _, _ in ARGS}

    nodes = [
        Node(
            package='active_perception',
            executable='live_camera',
            name='live_camera_node',
            output='screen',
            parameters=[{'camera_topic': c['camera_topic']}],
            condition=IfCondition(c['use_webcam']),
        ),
        Node(
            package='active_perception',
            executable='yolo_detector',
            name='yolo_detector_node',
            output='screen',
            parameters=[{'model_path': c['model_path'], 'target_class': c['target_object']}],
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
            parameters=[{'model': c['gemini_model'], 'env_file': c['env_file']}],
        ),
        Node(
            package='active_perception',
            executable='motion',  # no name override: the process holds two nodes
            output='screen',
            parameters=[{k: c[k] for k in (
                'orbit_radius', 'orbit_step_deg', 'orbit_direction', 'linear_speed',
                'angular_speed', 'min_angular_speed', 'cmd_vel_topic', 'odom_topic', 'scan_topic',
                'obstacle_stop_enabled', 'scan_front_angle_deg', 'use_arming', 'turn_source',
                'imu_topic', 'imu_yaw_sign', 'odom_turn_scale', 'scan_ignore_below',
                'robot_front_offset', 'obstacle_clearance', 'imu_gyro_scale', 'odom_distance_scale')}],
            condition=IfCondition(c['enable_motion']),
        ),
        Node(
            package='active_perception',
            executable='coordinator',
            name='coordinator_node',
            output='screen',
            parameters=[{k: c[k] for k in (
                'camera_topic', 'odom_topic', 'target_object', 'min_sharpness',
                'min_illumination', 'enable_motion', 'settle_sec', 'runs_dir')}],
        ),
        Node(
            package='active_perception',
            executable='interactive_trigger',
            name='interactive_trigger',
            prefix=c['trigger_prefix'],
            output='screen',
            condition=IfCondition(c['launch_trigger']),
        ),
        LogInfo(
            msg='Pipeline up. In another terminal run: ros2 run active_perception interactive_trigger',
            condition=UnlessCondition(c['launch_trigger']),
        ),
    ]

    return LaunchDescription(
        [DeclareLaunchArgument(name, default_value=default, description=desc)
         for name, default, desc in ARGS] + nodes)
