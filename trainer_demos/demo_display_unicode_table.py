#! /usr/bin/env python3
# Author: DCameron
# Description: This script will display the ENTIRE Unicode char set
"""
    Docstring:
"""

# ITERATE through all the char positions in the UNICODE table
# Using an INTERATOR for loop plus built-in range() function.
for pos in range(0, 65536):
    try:
        print(chr(pos), end=" ")
        if pos % 16 == 0:
            print()
    except UnicodeEncodeError:
        print(" ")