#! /usr/bin/env python3
# Author: DCameron
# Description: This module defines several BASIC calculator functions
"""
    Basic Calc functions - add, multiply and divide
"""
import sys

def add(*args):
    """ Return SUM of all the arguments
    >>> add(4, 3, 2)
    9
    """
    sum = 0
    for num in args:
        sum += num
    return sum

def mul(*args):
    """ Return PRODUCT of all the arguments
    >>> mul(4, 3)
    12
    >>> mul(4, 3, 2)
    24
    """
    product = 1
    for num in args:
        product *= num
    return product

def div(x, z):
    """ Return Quotient of x divided by z to 3 decimal places
    >>> div(4, 3)
    1.333
    """
    return round(x/z, 3)

def main():
    print("------------BASIC Calculator-------------")
    print(f"4 + 3 + 2 + 1 = {add(4, 3, 2, 1)}")
    print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
    print(f"4 / 3 = {div(4, 3)}")
    return None

# Namespace Trick
if __name__ == "__main__":
    # ONLY EXECUTE if ran directly as a script.
    # Ignore if imported as a module
    import doctest
    doctest.testmod()
    main()
    sys.exit(0)