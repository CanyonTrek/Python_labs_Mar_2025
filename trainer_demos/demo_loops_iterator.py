#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO ITERATE through
# a collection (str/tuple/list/dict/sets) using an ITERATOR
# for loop.
"""
    Docstring:
"""
#            0               1              2               3
heroes = ['elon musk', 'donald trump', 'bill gates', 'warren buffet',
          'ghandi', 'churchill', 'larry ellison', 'steve irwin']

# ITERATE through the LIST using ITERATOR for loop.
for name in heroes:
    print(name, end="\n")
print("Unchanged heroes=", heroes)

# ITERATE through the LIST using ITERATOR for loop and MODIFY objects.
idx = 0
for name in heroes:
    print(name.upper(), end="\n")
    heroes[idx] = name.upper()
    idx += 1
print("Changed heroes=", heroes)

# ITERATE through the LIST using ITERATOR for loop and MODIFY objects
# using the built-in emumerate() function.
for (idx, name) in enumerate(heroes, start=0):
    print(name.title(), end="\n")
    heroes[idx] = name.title()
print("Changed heroes=", heroes)