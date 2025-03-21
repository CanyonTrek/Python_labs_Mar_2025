#! /usr/bin/env python3
# Author: DCameron
# Description: This script is an ultra realistic calculator app
"""
    Calculator App with BASIC and ADVANCED functions
"""
import sys
# from basic import *
from basic import add, mul, div
# import basic
import adv

def main():
    while True:
        menu = """
                Calc Options
                ------------
                1. Basic calc examples
                2. Adv calc examples
                q = quit
        """
        print(menu)
        option = input("Enter option 1-2,q=quit: ")
        if option == 1:
            print(f"50 + 40 + 30 = {add(50, 40, 30)}")
            print(f"50 * 40 = {mul(50, 40)}")
            print(f"50 / 40 = {div(50, 40)}")
        elif option == 2:
            print(f"50 % 40 = {adv.mod(50, 40)}")
            print(f"50 ** 40 = {adv.power(50, 40)}")
            print(f"\N{square root}50 = {adv.sqrt(50)}")
        elif option == "q":
            break
        else:
            print("Invalid option")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)