#!/usr/bin/env python3
# import Metashape for processing
import Metashape
# argparse for using passed arguments
import argparse

# This script will be passed:
# frame_filepath as arg1, FRAME_LIMIT as arg2, frame_number as arg3
# Since the names of each frame is just frame_number.jpg,
# this script can use that fact to make a list of image filenames
# to be added to the metashape project.
# For now the idea is to have a "test" metashape project in my Documents
# folder, which will be blank when starting and is saved every time
# this script is called

# Save passed arguments into variables
frame_filepath = sys.argv[1]
FRAME_LIMIT = sys.argv[2]
frame_number = sys.argv[3]

# Set up Metashape document and chunk
# currently this doesn't work: there's a weird issue with Metashape
# returning a NoneType object when using Metashape.app.document
doc = Metashape.app.document
doc.open("/home/tanner/Documents/test.psx")
chunk = doc.addChunk()

# Build list of filenames based on FRAME_LIMIT, frame_number,
# and frame_filepath
first_frame = frame_number - FRAME_LIMIT
last_frame = frame_number
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
exportPoints(cloud_filename)
