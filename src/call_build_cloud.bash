#!/usr/bin/env bash

# NOTE: This file must be placed into your metashape pro folder, along
# with the file build_cloud.py

# Execute the build_cloud python script through metashape, passing along
# the arguments that came from metashape_node.py
# $1 -> frame_filepath, $2 -> FRAME_LIMIT, $3 -> frame_number
#sh ./metashape.sh -r build_cloud.py $1 $2 $3
sh ./metashape.sh -r test_script.py
