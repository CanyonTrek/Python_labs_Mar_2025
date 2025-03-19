#! /usr/bin/env python3
# Author: DCameron
# Description: This script will generate 6 UNIQUE random lottery numbers
"""
    Docstring:
"""
import random
lotto = [] # Empty list

while len(lotto) < 6:
    num = random.randint(1, 50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("Duplicate number =", num)


print("Lottery numbers =", lotto)