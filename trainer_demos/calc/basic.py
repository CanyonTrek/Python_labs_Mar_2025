#! /usr/bin/env python3
# Author: DCameron
# Description: This module defines several BASIC calculator functions
"""
    Basic Calc functions - add, multiply and divide
"""
import sys

def add(*args):
    """ Return SUM of all the arguments """
    sum = 0
    for num in args:
        sum += num
    return sum

def mul(*args):
    """ Return PRODUCT of all the arguments """
    product = 1
    for num in args:
        product *= num
    return product

def div(x, z):
    """ Return Quotient of x divided by z to 3 decimal places """
    return round(x/z, 3)

print("------------BASIC Calculator-------------")
print(f"4 + 3 + 2 + 1 = {add(4, 3, 2, 1)}")
print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
print(f"4 / 3 = {div(4, 3)}")

sys.exit(0)