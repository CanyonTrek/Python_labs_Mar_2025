#! /usr/bin/env python3
# Author: DCameron
# Description: This module defines a class of Tank
"""
    Tank Class for an online game
"""
import vehicle

class Tank(vehicle.Vehicle):
    # Class has 2 components = Attributes/Data + Behaviour/Methods
    def __init__(self, country, model):
        super().__init__(country, model)
        self._location = {'x':0, 'y':0, 'z':0}
        self._direction = 0
        self._health = 100
        self._shells = 20
        # No explicit return as this method is called implicitly

    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None

    def __del__(self):
        print("Booom..tank has been destroyed")
        return None

    # SPECIAL Methods
    # Example of Operator Overloading
    def __add__(self, other):
        return self._health + other._health

    # Example of DUCK Typing - our Tank can now QUACK like a DUCK!
    def __str__(self):
        return f"Model={self.model}, Speed={self._speed}, Health={self._health}"

    # Example of a GETTER and SETTER method
    def get_health(self):
        return self._health

    def set_health(self, new_health):
        self._health = new_health
        return None

    # Wrap one variable name INTERFACE to getter/setter methods.
    tank_health = property(get_health, set_health)