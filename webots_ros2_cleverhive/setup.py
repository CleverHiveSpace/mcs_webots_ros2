from setuptools import setup
import os
package_name = 'webots_ros2_cleverhive'

def collect_files_recursively(directory, package_name):
    """
    Recursively collect files from a directory and format them for data_files.
    
    Args:
        directory (str): Directory to scan recursively
        package_name (str): Name of the package
        
    Returns:
        list: List of tuples (destination_path, [file_paths]) for data_files
    """
    collected_files = []
    if os.path.exists(directory):
        for root, dirs, files in os.walk(directory):
            if files:
                # Create relative path from the directory
                relative_path = root
                # Create destination path in the share directory
                dest_path = os.path.join('share', package_name, relative_path)
                # Add files with their paths
                collected_files.append((dest_path, [os.path.join(root, f) for f in files]))
    return collected_files


data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/rosbot_launch.py']))
data_files.append(('share/' + package_name + '/resource', ['resource/rosbot_controllers.yaml']))
data_files.append(('share/' + package_name + '/resource', ['resource/ekf.yaml']))
data_files.append(('share/' + package_name + '/resource', ['resource/laser_filter.yaml']))
data_files.append(('share/' + package_name + '/resource', ['resource/rosbot_webots.urdf']))
data_files.append(('share/' + package_name + '/resource', ['resource/rosbot_links_remappings.yaml']))
data_files.append(('share/' + package_name, ['package.xml']))
data_files.extend(collect_files_recursively('protos', package_name))
data_files.extend(collect_files_recursively('worlds', package_name))




setup(
    name=package_name,
    version='2023.0.4',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    author='Jakub Delicat',
    author_email='jakub.delicat@husarion.com',
    maintainer='Husarion',
    maintainer_email='support@husarion.com',
    keywords=['ROS', 'Webots', 'Robot', 'Simulation', 'Examples', 'ROSbot', 'ROSbot 2R', 'ROSbot XL', 'Husarion'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Husarion ROSbot 2R and XL robots ROS2 interface for Webots.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
