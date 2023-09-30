from setuptools import setup

package_name = 'vision_rpi_bot'


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='asif',
    maintainer_email='asif@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f'vision_rpi_bot_publisher = vision_rpi_bot.publisher:main',
            f'vision_rpi_bot_subscriber = vision_rpi_bot.subscriber:main',
        ],
    },
)

