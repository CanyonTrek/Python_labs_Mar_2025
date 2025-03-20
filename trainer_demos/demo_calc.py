#! /usr/bin/env python3
# Author: DCameron
# Description: This script will simulate a calculator with simple
# functions for adding, multiplying and dividing.
"""
    Calc App with add, multiply and divide functions.
"""
def add(x, z):
    """ Return sum of x and z as a float """
    return float(x + z)

def mul(x, z):
    """ Return Product of x and z as a float """
    return float(x*z)

def div(x, z):
    """ Return quotient of x divided by z to 3 decimal places """
    return round(x/z, 2)

print(f"4 + 3 = {add(4, 3)}")
print(f"4 * 3 = {mul(4, 3)}")
print(f"4 / 3 = {div(4, 3)}")

# Alternatively, we could DEFINE a user function using the lambda statement
# which allows us to create a ONE-LINER function definition.
l_add = lambda x, z: float(x + z)
l_mul = lambda x, z: float(x * z)
l_div = lambda x, z: round(x/z, 2)

print(f"4 + 3 = {l_add(4, 3)}")
print(f"4 * 3 = {l_mul(4, 3)}")
print(f"4 / 3 = {l_div(4, 3)}")
