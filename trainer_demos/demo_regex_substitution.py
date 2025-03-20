#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO to match and SUBSTITUTE a pattern
# with a string using the re.sub() or re.subn() functions.
"""
    Docstring:
"""
import re

# Sample from /etc/passwd on Linux for the root user account.
line = "root:x:0:0:The Super User:/root:/bin/ksh"
# AND I want to make some changes to string! IMMUTABLE! :-(
line = re.sub(r"[sS]uper [uU]ser", r"Administrator", line) # Returns a NEW str object.
(line, num) = re.subn(r"ksh$", r"bash", line) # Returns a TUPLE (new str, num changes)

print(f"Modified string = {line} with {num} changes")