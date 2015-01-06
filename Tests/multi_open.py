#!/usr/bin/python3
# project         :EchoTags
# title           :multi_open
# description     :Learning to open and process multiple files
# author          :ravila
# date            :1/5/15
# version         :
# usage           :
# notes           :
# python_version  :3.4
# ==============================================================================


# A loop for cycling through several files when these are opened with a wildcard.
#
# e.g. 'python3 multi_open.py *.mp3 mp3'
#
# System arguments are given indexes that start from 0.
# Therefore, in this example, 'multi_open.py' has index 0,
# every file in the folder with the extension '.mp3' has an index starting from 1
# to whatever number of .mp3's we have. Finally, the string 'mp3' has the last index.


import sys
x = len(sys.argv) - 1  # This gives us the number of arguments passed.
file_type = sys.argv[x]  # Set 'type' equal to the last argument passed.

for f in range(1, x):
    print(str(sys.argv[f]), sys.argv[x])