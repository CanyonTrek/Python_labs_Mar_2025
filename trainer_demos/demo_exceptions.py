#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo different ways of dealing with
# an ERROR/EXCEPTION
"""
    Docstring:
"""

num = 42
txt = "3"

# Fix 1: Convert str into int
if int(txt) < num:
    print("Less than")
else:
    print("greater than")

# Fix 2: Check what type of data they are.
if isinstance(txt, int):
    if txt < num:
        print("Less than")
    else:
        print("greater than")
else:
    print("Cannot compare str and int with '>'")


# Fix 3: Check what type of data they are.
try:
    if txt < num:
        print("less than")
    else:
        print("greater than")
except TypeError:
    print("Cannot compare txt and num")