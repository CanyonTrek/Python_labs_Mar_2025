#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO create, and grow, and shrink SETS
# (Unordered Collections with Unique VALUES)
"""
    Docstring:
"""

marvel_fans = {'donald', 'grace', 'isla', 'david', 'john'}
dc_fans = set() # Empty SET

# GROW a SET
dc_fans.add('donald')
dc_fans.add('rohit')

# Copy, Shrink and clear SETS
# comic_fans = dc_fans.copy() # Copy SET
# comic_fans.pop() # RANDOMLY remove VALUE
# comic_fans.clear() # Empty SET

# PRINT/COMBINE SETS using SET operators (Remember VENN diagrams).
print(f"Fans of BOTH Marvel OR DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of BOTH Marvel AND DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY Marvel = {marvel_fans.difference(dc_fans)}")
print(f"Fans of EITHER Marvel OR DC = {marvel_fans.symmetric_difference(dc_fans)}")
print("-" * 60)
# PRINT/COMBINE SETS using SET operators (Remember VENN diagrams).
print(f"Fans of BOTH Marvel OR DC = {marvel_fans | dc_fans}")
print(f"Fans of BOTH Marvel AND DC = {marvel_fans & dc_fans}")
print(f"Fans of ONLY Marvel = {marvel_fans - dc_fans}")
print(f"Fans of EITHER Marvel OR DC = {marvel_fans ^ dc_fans}")