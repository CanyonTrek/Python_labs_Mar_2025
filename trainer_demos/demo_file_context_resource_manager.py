#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO a SAFER way to open file handles
# using the with statement (Context Resource Manager)
"""
    Docstring:
"""
movies = { 'rohit': ['internal affairs', 'inside out', 'death at a funeral'],
           'david': ['borat', 'grimsby', 'dictator'],
           'donald': ['lotr', 'the hobbit', 'brave'],
           'isla': ['avengers', 'winter soldier', 'age of ultron']
}

file = r"C:\Users\Donal\course\Python_labs_Mar_2025\trainer_demos\movies.txt"

with open(file, mode="wt") as fh_out:
    for name in movies.keys():
        print(f"{name}: {movies[name]}", end="\n")
        fh_out.write(f"{name}: {movies[name]}\n")
    # End of block, fh_out is closed

print("-" * 60)

with open(file, mode="rt") as fh_in:
    for line in fh_in:
        print(line, end="")

