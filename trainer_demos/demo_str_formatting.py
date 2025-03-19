#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO format strings in different ways
# using str concatenation and escape chars, str justification methods, the
# .format() method and f-strings!
"""
    Docstring:
"""
# Random data for planets and their distance to SUN in gigametres.
planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}

# ITERATE through the planets keys and print planet info
# Using ITERATOR for loop plus str concatenation and escape chars MEH!
for planet in planets.keys():
    print("\t\t" + planet + ": " + str(planets[planet]) + " Gm\t" + str(hex(0xff)))

print("-" * 40)
# Using ITERATOR for loop plus str justification methods! ok!
for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).rjust(12, '.') + " Gm" + str(hex(0xff)).rjust(6))

print("-" * 40)
# Using ITERATOR for loop plus str.format() method! GOOD!
for planet in planets.keys():
    print("{0:>12s}: {1:12.3f} Gm {2:#5x}".format(planet, planets[planet], 0xff))

print("-" * 40)
# Using ITERATOR for loop plus f-strings (Py 3.5 onwards)! My favourite!
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:12.3f} Gm {0xff:#5x}")
