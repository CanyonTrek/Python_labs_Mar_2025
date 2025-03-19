#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO match text data from a file
# using str testing and pattern matching - using the re module.
"""
    Docstring:
"""
import re

# Open file handle for READING in TEXT mode.
fh_in = open(r"C:\Users\Donal\course\Python_labs_Mar_2025\labs\words", mode="rt")

reobj = re.compile(r"^([A-Z]).*\1$") # Precompile Pattern ONCE!

for line in fh_in:
    # m = re.search(r"^([A-Z]).*\1$", line)  # MATCH lines start/end SAME CAPITAL
    m = reobj.search(line)  # USE Precompiled PATTERN!
    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")


fh_in.close() # Close file handle.