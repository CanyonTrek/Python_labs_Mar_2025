#! /usr/bin/env python3
# Author: DCameron
# Description: This module defines a BASE class of Vehicle for Tanks and Jeeps
"""
    Vehicle Base Class
"""

class Vehicle:
    def __init__(self, country, model):
        self.country = country
        self.model = model
        self._speed = 0

    def accel(self, increase):
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed -= decrease
        return None