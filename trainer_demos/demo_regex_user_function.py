#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO match text data from a file
# using str testing and pattern matching - using the re module.
"""
    Docstring:
"""
import re

# Example of a user function with optional parameter passing and
# default values.
def search_pattern(pattern=r"^.{19}$", file=r"C:\Users\Donal\course\Python_labs_Mar_2025\labs\words"):
    lines = 0
    # Open file handle for READING in TEXT mode.
    with open(file, mode="rt") as fh_in:
        for line in fh_in:
           m = re.search(pattern, line)  # MATCH lines start/end SAME CAPITAL
           if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
    return lines

lines_matched = 0
lines_matched += search_pattern()
lines_matched += search_pattern(r"^([A-Z]).*\1$",
                                file=r"C:\Users\Donal\course\Python_labs_Mar_2025\labs\words")
print(f"Lines matched = {lines_matched}")