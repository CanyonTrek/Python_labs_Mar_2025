#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO split and join strings
# using the .split() and .join() methods.
"""
    Docstring:
"""
# A sample line from /etc/passwd on Linux for the root user account.
line = "root:x:0:0:The Super User:/root:/bin/ksh"

# I need to modify but str are Immutable!
fields = line.split(":") # Returns a LIST (which is MUTABLE)
fields[4] = "The Administrator"
fields[6] = "/bin/bash"
line = ":".join(fields) # Return a NEW str!
print("Modified line=", line)