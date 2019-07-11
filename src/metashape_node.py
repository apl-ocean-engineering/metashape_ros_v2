#!/usr/bin/env python
from __future__ import print_function
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
# Subprocess for starting the bash script
import subprocess
# argparse for saving frames to desired location
import argparse

# How this works:
# This ROS node subscribes to an image topic being published by the kinect
# and saves each frame to disk. After FRAME_LIMIT number of frames have
# been saved, this node will call a bash script from within the metashape
# folder on this machine, passing along the filepath to all saved frames,
# the current frame number as well as FRAME_LIMIT. The bash script will
# execute another python script, which will add the last FRAME_LIMIT
# number of frames to a metashape project, align them, generate a
# dense point cloud, then save the result.

# Note: the user must pass the a filepath to the folder where they want
# the frames saved to.


# Number of frames that have been processed
frame_number = 0
# Instantiate CvBridge
bridge = CvBridge()
# How many frames should be saved before generating dense point cloud
FRAME_LIMIT = 0
# Path where the bash script + build_cloud.py are located
BASH_SCRIPT_PATH = "/home/tanner/metashape-pro/call_build_cloud.sh"

def image_callback(msg):
    frame_number += 1
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError:
        print("cvbridge failed!")

    # Create filename for current frame, based on frame_number
    # as well as filepath specified by user
    try:
        frame_filepath = sys.argv[1] + "/"
    except IndexError:
        print("Filepath for saving frames was not given.")
        print("Please include the full filepath of where you'd like frames to be saved.")
        print("Ex: /home/tanner/code/metashape_node/images/test")
    frame_number_string = str(frame_number)
    frame_filename = frame_filepath + frame_number_string + ".jpeg"

    # Save the current frame to the given filepath, according to its frame number
    # TODO: see if you can save raw images instead of jpeg for higher quality
    cv2.imwrite(frame_filename, cv2_img)

    # Determine whether to build dense point cloud
    if (frame_number % FRAME_LIMIT) == 0:
        # Execute bash script to build and save dense point cloud
        subprocess.call([BASH_SCRIPT_PATH, frame_filepath, FRAME_LIMIT, frame_number])


def main():
    rospy.init_node('metashape_node', anonymous=True)
    # Define your image topic
    image_topic = "/camera/rgb/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)
    # Spin until ctrl + c
    rospy.spin()


if __name__ == '__main__':
    main()
