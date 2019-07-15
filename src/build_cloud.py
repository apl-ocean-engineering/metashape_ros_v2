#!/usr/bin/env python3
# import Metashape for processing
import Metashape
# argparse for using passed arguments
import argparse
import os
import sys
import time
# This script will be passed:
# frame_filepath as arg1, FRAME_LIMIT as arg2, frame_number as arg3
# Since the names of each frame is just frame_number.jpg,
# this script can use that fact to make a list of image filenames
# to be added to the metashape project.
# Be sure to set a filepath for the metashape project file this script
# will use and modify as it runs

# Save passed arguments into variables
frame_filepath = sys.argv[1]
FRAME_LIMIT = int(sys.argv[2])
frame_number = int(sys.argv[3])

# User-defined filepath for the metashape project used by this script
METASHAPE_PROJECT_PATH = "/home/tanner/code/metashape_node/project/test.psx"

# Set up Metashape document and chunk
doc = Metashape.Document()
try:
    doc.open(METASHAPE_PROJECT_PATH)
    chunk = doc.chunks[0]
except OSError:
    chunk = doc.addChunk()

# GPU mask to force usage of gpu for calculations
Metashape.app.gpu_mask = 2 ** (len(Metashape.app.enumGPUDevices())) - 1

# Build list of filenames based on FRAME_LIMIT, frame_number,
# and frame_filepath
first_frame = frame_number - FRAME_LIMIT
last_frame = frame_number
frame_list = []
for current_frame_num in range(first_frame, last_frame):
    current_frame_filepath = frame_filepath + str(current_frame_num) + ".JPG"
    frame_list.append(current_frame_filepath)

# Add frame_list to chunk in metashape
chunk.addPhotos(frame_list)

# Align cameras and build dense cloud
start_time = time.time()
chunk.matchPhotos(accuracy=Metashape.LowestAccuracy)
print("Photo matching took", time.time() - start_time, "to run")
chunk.alignCameras()
start_time = time.time()
chunk.buildDepthMaps(quality=Metashape.LowestQuality)
print("Depth maps took", time.time() - start_time, "to run")
chunk.buildDenseCloud()

# Save generated dense cloud to same location as frames
cloud_filename = frame_filepath + "cloud_" + str(frame_number) + ".obj"
chunk.exportPoints(cloud_filename)

# Save changes made to the metashape project
doc.save(METASHAPE_PROJECT_PATH)
