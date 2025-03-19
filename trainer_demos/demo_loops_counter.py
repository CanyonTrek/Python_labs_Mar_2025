#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO repeat a block of
# commands a specific number of repetitions using a COUNTER loop.
"""
    Docstring:
"""

count = 0 # 1.Initialise counter
while count < 10: # 2.Test counter
    print(count)
    count += 1 # 3.Increment counter

# Alternatively we could write a COUNTER loop
# using a for loop plus built-in range(start, stop, step) function.
for num in range(0, 10, 1):
    print(num)

# using a for loop plus built-in range(start=0, stop, step) function.
for num in range(10, 1):
    print(num)

# using a for loop plus built-in range(start=0, stop, step=1) function.
for num in range(10):
    print(num)