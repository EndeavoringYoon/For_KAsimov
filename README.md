# For_KAsimov
Environments: Ubuntu 22.04 ros2 humble, Anaconda python 3.10.8, Dynamixel SDK example with profile velocity 150, profile acceleration 10

# You need To...
Dynmixel_SDK humble-devel(https://github.com/ROBOTIS-GIT/DynamixelSDK.git) with modification in cmake_minimum_required(VERSION) in CMakeLists.txt-appropriate to your cmake version(in my case: VERSION 3.26)
For colcon build errors that I suffered while building SDK, check this notion(https://www.notion.so/ROS2-with-Dynamixel-b2b53e7c61024f96aeaa653c957154fe?pvs=4)
![example](./images/example_openmanipulator.gif)
