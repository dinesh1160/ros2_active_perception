from setuptools import find_packages
from setuptools import setup

setup(
    name='active_perception_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('active_perception_interfaces', 'active_perception_interfaces.*')),
)
