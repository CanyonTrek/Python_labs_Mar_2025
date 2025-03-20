#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO create a generator function to
# yield one object at a time.
"""
    Docstring:
"""

def get_numbers():
    """ Return a list of numbers """
    numbers = []
    for x in range(0, 10):
        numbers.append(x)
    return numbers

def generate_numbers():
    """ Yield one object from a collection at a time """
    print("Executing generate_numbers..")
    for x in range(0, 10):
        yield x


# for z in get_numbers():
for z in generate_numbers():
    print(z)

# An alternative way of using a generator function using a while loop.
gen = generate_numbers()
while True:
    num = next(gen, -1)
    if num != -1:
        print(num)
    else:
        break

# Alternatively, we could request next yielded value manually..
gen = generate_numbers()
num1 = next(gen)
num2 = next(gen)
num3 = next(gen)
print(num1, num2, num3)

