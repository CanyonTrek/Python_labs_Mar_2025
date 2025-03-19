#! /usr/bin/env python3
# Author: DCameron
# Description: This script will simulate a high street bank PIN
# machine
"""
    Docstring:
"""
import sys
import getpass

master_pin = "0123"
pin = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = getpass.getpass("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")
        attempts += 1
else:
    # Execute ONCE only when LOOP naturally ends.
    print("Too many attempts")
    print("Your card has been retained. Have a nice day!")


print("Done")
# sys.exit(0) # EXPLICIT EXIT script with return code (0=success, 1-255=error code)
# sys.exit(66) # EXIT script with return code (0=success, 1-255=error code)
sys.exit("goodbye") # EXIT with expression (STDERR) return code=1
