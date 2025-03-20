#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO define a user function, call it
# and optionally pass parameters IN and data back OUT
"""
    Docstring:
"""
from os import statvfs_result
from types import NoneType


# Example of a USER function with parameter passing
# and default values. Annotations - embedded help to indicate
# preferred datatype BUT not enforced!
def say_hello(greeting:str='namaste', recipient:str='dost')->None:
    message = f"{greeting} {recipient}"
    print(message)
    return None


say_hello('hello', 'my friends') # Positional parameter passing
say_hello(greeting='bonjour', recipient='mes amis') # Named parameter passing
say_hello('hola', recipient='amigos') # Mix parameter passing (positional->named)
say_hello(recipient='amici', greeting='ciao') # Named parameter passing in different order
say_hello('namaste', 3.14)
say_hello()

print(f"Annotations for say_hello = ", say_hello.__annotations__) # Fact finding