#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO match text data from a file
# using str testing and pattern matching - using the re module.
"""
    Module with search routines for searching for Regex patterns
    in files.
"""
import re

# Example of a VARIADIC function that allows variable number of parameters
# which are captured in a TUPLE!
def search_pattern(pattern=r"^.{19}$", *files):
    """ Search for a Regex pattern in one or more files and return lines matched """
    lines = 0
    for file in files:
        # Open file handle for READING in TEXT mode.
        with open(file, mode="rt") as fh_in:
            for line in fh_in:
               m = re.search(pattern, line)  # MATCH lines start/end SAME CAPITAL
               if m:
                    lines += 1
                    print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
    return lines

lines_matched = 0
lines_matched += search_pattern(r"^([A-Z]).*\1$", r"c:\labs\words", r"c:\labs\words2")
print(f"Lines matched = {lines_matched}")