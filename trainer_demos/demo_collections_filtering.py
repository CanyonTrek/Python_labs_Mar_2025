#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO copy a SOURCE collection
# to a DESTINATION with optional filtering..
"""
    Docstring:
"""

students = ['rohit', 'john', 'david', 'donald', 'meredith', 'reacher', 'isla', 'david']

# Copy source collection to a destination and filter out the long names!
# 1.Using an ITERATOR loop + source, optional condition (filtering), expression
wee_names = []
for name in students: # 1.Iterator loop plus source
    if len(name) <= 5: # 2.If condition (optional filtering)
        wee_names.append(name.upper()) # 3.expression
print(f"1.Short names = {wee_names}")

def filter_names(name):
    """ Return True if name parameter is <= 5 chars """
    if len(name) <= 5:
        return True
    else:
        return False

# 2.Using an ITERATOR loop + source, user function (filtering), expression
wee_names = []
for name in students:
    if filter_names(name):
        wee_names.append(name.upper())
print(f"2.Short names = {wee_names}")

# 3.Using the built-in filter() + source,  user function (filtering).
wee_names = list(filter(filter_names, students))
print(f"3.Short names = {wee_names}")

# 4.Using the built-in filter() + source,  lambda function (filtering).
wee_names = list(filter(lambda name:len(name) <= 5, students))
print(f"4.Short names = {wee_names}")

# 5.Using LIST COMPREHENSION - expression, iterator loop plus source, optional condition.
wee_names = [ name.upper() for name in students if len(name) <= 5 ]
print(f"5.Short names = {wee_names}")

# 5.1.Using LIST COMPREHENSION - expression, iterator loop plus source, optional condition.
wee_names = [ (name.upper(), len(name)) for name in students if len(name) <= 5 ]
print(f"5.1.Short names = {wee_names}")

# 5.2.Using DICT COMPREHENSION - expression, iterator loop plus source, optional condition.
# EXTRA filtering - Keys must be Unique!
wee_names = { name.upper(): len(name) for name in students if len(name) <= 5 }
print(f"5.2.Short names = {wee_names}")

# 5.3.Using SET COMPREHENSION - expression, iterator loop plus source, optional condition.
# EXTRA filtering - VALUES must be Unique!
wee_names = { name.upper() for name in students if len(name) <= 5 }
print(f"5.3.Short names = {wee_names}")
