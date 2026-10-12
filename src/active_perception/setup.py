from glob import glob

from setuptools import find_packages, setup

package_name = 'active_perception'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bluegoose',
    maintainer_email='dinesharunachalam116@gmail.com',
    description='Active perception: pick the best camera angle with YOLO, heuristics and a VLM',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'live_camera = active_perception.live_camera_node:main',
            'yolo_detector = active_perception.yolo_detector_node:main',
            'heuristic_scorer = active_perception.heuristic_scorer:main',
            'vlm_bridge = active_perception.vlm_bridge_node:main',
            'coordinator = active_perception.coordinator_node:main',
            'interactive_trigger = active_perception.interactive_trigger:main',
        ],
    },
)
