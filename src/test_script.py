#!/usr/bin/env python3
# import Metashape for processing
import Metashape
# argparse for using passed arguments
import argparse
import os
import sys

# test script for making a dense point cloud
# uses images from beginner doll tutorial

first_frame = 1000
last_frame = 1059
frame_filepath = "/home/tanner/Downloads/doll/"

doc = Metashape.Document()
chunk = doc.addChunk()
frame_list = []
for current_frame_num in range(first_frame, last_frame):
    current_frame_filepath = frame_filepath + "IMG_" + str(current_frame_num) + ".JPG"
    frame_list.append(current_frame_filepath)

#chunk.addCamera()
chunk.addPhotos(frame_list)
chunk.matchPhotos()
chunk.alignCameras()
chunk.buildDepthMaps()
chunk.buildDenseCloud()
doc.save("/home/tanner/Desktop/test.psx")
# Save generated dense cloud to same location as frames
#cloud_filename = frame_filepath + "cloud_" + str(frame_number) + ".obj"
#Metashape.exportPoints(cloud_filename)
