#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""
import basic

def test_add():
    assert basic.add(4, 3) == 7, "Error should be 7"
    assert basic.add(4, 3, 2) == 9, "Error should be 9"
    return None

def test_mul():
    assert basic.mul(4, 3) == 12, "Error should be 12"
    assert basic.mul(4, 3, 2) == 24, "Error should be 24"
    return None

def test_div():
    assert basic.div(4, 3) == 1.334, "Error should be 1.333"
    return None

def main():
    print("Starting tests...")
    test_add()
    test_mul()
    test_div()
    print("Tests ALL successful")
    return None

if __name__ == "__main__":
    main()