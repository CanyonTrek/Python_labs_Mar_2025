#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO check which platform
# your script is running on?
"""
    Docstring:
"""

import sys
import os
import glob

if sys.platform == "win32":
    print("Running on a windows platform")
    home = os.environ["HOMEPATH"]
    pattern = home + r"\*"
else:
    print("Running on Linux")
    home = os.environ["HOME"]
    pattern = home + r"/*"

print("Home directory is", pattern)


files = glob.glob(pattern) # Return list of files + dirs
print(files)

# Iterate through LIST using an ITERATOR for loop.
for file in files:
    if os.path.isfile(file):
        size = os.path.getsize(file)
        print(file, size, end="\n")


