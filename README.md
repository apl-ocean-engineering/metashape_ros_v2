# metashape_ros_v2
ROS node and scripts for attempting 'realtime' reconstruction using ROS and Metashape

## Installation
Add metashape_ros_v2 to your catkin_ws/src folder, then run catkin_make from your catkin_ws directory

## Usage
  * Currently I am using [openni_launch](http://wiki.ros.org/openni_launch) to get images from a kinect
  * The files **build_cloud.py and call_build_cloud.bash must be located in your metashape-pro folder**
  * The ROS node metashape_node.py requires you to pass a filepath to a folder where you would like the frames captured by your camera to be saved
  * -To be updated once things are more fleshed out-

## Miscellaneous Info
How this works: the ROS node subscribes to an image topic being published by the kinect and saves each frame to disk. After a specified number of frames have been saved, the node then executes call_build_cloud.bash, which in turn runs a python script running through Metashape. The python script running through Metashape then adds any new frames to the Metashape project, aligns them, generates a dense point cloud, and saves the result.

## License
[MIT](https://choosealicense.com/licenses/mit/)
