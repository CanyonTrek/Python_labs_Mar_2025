#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""
import unittest # This module provides a TEST RUNNER
from .. import basic

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(basic.add(4, 3), 7.2, "Error should be 7")
        self.assertEqual(basic.add(4, 3, 2), 9.1, "Error should be 9")
        return None

    def test_mul(self):
        self.assertEqual(basic.mul(4, 3), 13, "Error should be 12")
        self.assertEqual(basic.mul(4, 3, 2), 24, "Error should be 24")
        return None

    def test_div(self):
        self.assertEqual(basic.div(4, 3), 1.335, "Error should be 1.333")
        return None

if __name__ == "__main__":
    unittest.main()