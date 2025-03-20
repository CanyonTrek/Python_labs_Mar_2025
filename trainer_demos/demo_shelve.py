#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO preserve MULTIPLE Python objects
# into ONE file using the SHELVE module
"""
    Docstring:
"""
import shelve
import pprint

movies = { 'rohit': ['internal affairs', 'inside out', 'death at a funeral'],
           'david': ['borat', 'grimsby', 'dictator'],
           'donald': ['lotr', 'the hobbit', 'brave'],
}
tv_series = { 'rohit': ['GOT', 'reacher'],
           'david': ['simpsons', 'neighbours'],
           'donald': ['outlander', 'the boys'],
}
books = { 'rohit': 'lion, witch and wardrobe',
           'david': "dummy's guide to python",
           'donald': 'guide to trainsets'
}

with shelve.open(r"C:\Users\Donal\course\Python_labs_Mar_2025\trainer_demos\media") as db:
    db['movies'] = movies
    db['tv_series'] = tv_series
    db['books'] = books


with shelve.open(r"C:\Users\Donal\course\Python_labs_Mar_2025\trainer_demos\media") as db:
    print(f"Rohit's favourite movies are {db['movies']['rohit']}")
    print(f"Donald's favourite tv_series are {db['tv_series']['donald'][0]}")
    print(f"David's favourite book is {db['books']['david']}")






