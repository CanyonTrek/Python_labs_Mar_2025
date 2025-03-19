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

# Iterate through the file handle one line at a time.
for line in fh_in:
    # Example of str testing.
    # if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    # m = re.search(r"the", line) # Match lines with 'the'.
    # m = re.search(r"^the", line)  # Match lines starting with 'the'.
    # m = re.search(r"ing$", line)  # Match lines ending with 'ing'.
    # m = re.search(r"^ring$", line)  # Match lines exactly with 'ring'.
    # m = re.search(r"^.ing$", line)  # Match lines with char followed by 'ing'.
    # m = re.search(r"^[adrp]ing$", line)  # Match lines with [adrp] followed by 'ing'.
    # m = re.search(r"^[adrp]ing$", line)  # Match lines with [adrp] followed by 'ing'.
    # m = re.search(r"^[A-Z]", line)  # Match lines start with CAPITAL.
    # m = re.search(r"^...................$", line)  # Match lines EXACTLY 19 chars
    # m = re.search(r"^.{19}$", line)  # Match lines EXACTLY 19 chars
    # m = re.search(r"[aeiou][aeiou][aeiou]", line)  # Match lines with 3 consecutive vowels.
    # m = re.search(r"[aeiou]{5,}", line)  # Match lines with at least 5 consecutive vowels.
    # m = re.search(r"\.", line)  # Match lines with a DOT.
    # m = re.search(r"[.]", line)  # Match lines with a DOT.
    # m = re.search(r"^[A-Z].*[A-Z]$", line)  # Match lines START/END with CAPITAL
    # m = re.search(r"^[A-Z].{4}[A-Z]$", line)  # Match lines of 6 chars START/END with CAPITAL
    # m = re.search(r"^(.)(.).\2\1$", line, flags=re.IGNORECASE)  # Match 5 char Palindromes
    # m = re.search(r"^([A-Z]).*\1$", line)  # Match lines start/end with SAME CAPITAL!
    # m = re.match(r"([A-Z]).*\1$", line)  # AUTO MATCH lines starting with pattern!
    m = re.fullmatch(r"^([A-Z]).*\1\n$", line)  # MUST MATCH ENTIRE LINE + hidden chars!
    if m:
        # m.group() is the pattern, m.start() is where pattern starts.
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}, "
              f"Groupings={m.groups()}, group 1 = {m.group(1)}") # Must use Groupings!


fh_in.close() # Close file handle.