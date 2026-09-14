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
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bluegoose',
    maintainer_email='dinesharunachalam116@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'mock_camera = active_perception.mock_camera_node:main',
            'mock_detector = active_perception.mock_detector_node:main',
            'heuristic_scorer = active_perception.heuristic_scorer:main',
        ],
    },
)
