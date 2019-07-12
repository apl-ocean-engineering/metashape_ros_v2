#!/usr/bin/env python3
# import Metashape for processing
import Metashape
# argparse for using passed arguments
import argparse
import os
import sys

# This script will be passed:
# beginning and end indexes of photo frame numbers to align / use
# filepath of where to save the result

# adapting this thing to the doll photoset
first_frame = 1000
last_frame = 1059
frame_filepath = "/home/tanner/Downloads/doll/"

doc = Metashape.Document()
chunk = doc.addChunk()
frame_list = []
for current_frame_num in range(first_frame, last_frame):
    current_frame_filepath = frame_filepath + "IMG_" + str(current_frame_num) + ".JPG"
    frame_list.append(current_frame_filepath)
    
chunk.addCamera()
chunk.addPhotos(frame_list)
chunk.alignCameras()
chunk.buildDenseCloud()

# Save generated dense cloud to same location as frames
cloud_filename = frame_filepath + "cloud_" + str(frame_number) + ".obj"
Metashape.exportPoints(cloud_filename)

'''
# Save passed arguments into variables
first_frame = sys.argv[1]
last_frame = sys.argv[2]
frame_filepath = sys.argv[3]

# Set up Metashape document and chunk
# going to be using a project "test.psx" that already exists and has
# one chunk available for use
doc = Metashape.Document()
doc.open("/home/tanner/code/metashape_node/project/test.psx")
chunk = doc.chunks()

# Build list of filenames
frame_list = []
for current_frame_num in range(first_frame, last_frame):
    current_frame_filepath = frame_filepath + str(current_frame_num) + ".jpeg"
    frame_list.append(current_frame_filepath)

# Add frame_list to chunk in metashape
chunk.addPhotos(frame_list)

# Align cameras and build dense cloud
chunk.alignCameras()
chunk.buildDenseCloud()

# Save generated dense cloud to same location as frames
cloud_filename = frame_filepath + "cloud_" + str(frame_number) + ".obj"
Metashape.exportPoints(cloud_filename)
'''
