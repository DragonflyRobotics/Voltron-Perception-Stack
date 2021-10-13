from setuptools import setup

package_name = 'yolo_ai'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Krishna',
    maintainer_email='krishna@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = yolo_ai.publisher_member_function:main',
            'listener = yolo_ai.subscriber_member_function:main',
        ],
    },
)
