#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO match text data from a file
# using str testing and pattern matching - using the re module.
"""
    Docstring:
"""
import re
import sys

# Example of a user function with optional parameter passing and
# default values.
def search_pattern(pattern=r"^.{19}$", file=r"C:\Users\Donal\course\Python_labs_Mar_2025\labs\words"):
    lines = 0
    # Open file handle for READING in TEXT mode.
    with open(file, mode="rt") as fh_in:
        reobj = re.compile(pattern) # Precompile pattern ONCE
        for line in fh_in:
           # m = re.search(pattern, line)  # MATCH lines start/end SAME CAPITAL
           m = reobj.search(line)
           if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
    return lines

def main():
    lines_matched = 0
    lines_matched += search_pattern()
    print(f"Lines matched = {lines_matched}")
    return None

if __name__ == "__main__":
    import cProfile
    # cProfile.run("main()") # Analysis to the console
    cProfile.run("main()", "stats.prof")  # Analysis to a file
    # main()
    sys.exit(0)