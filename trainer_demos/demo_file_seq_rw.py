#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO open, close, and read, write
# and append to a TEXT file using the built-in open() function.
"""
    Docstring:
"""
import sys
movies = { 'rohit': ['internal affairs', 'inside out', 'death at a funeral'],
           'david': ['borat', 'grimsby', 'dictator'],
           'donald': ['lotr', 'the hobbit', 'brave'],
           'isla': ['avengers', 'winter soldier', 'age of ultron']
}

# Open file handle for WRITING in TEXT mode
file = r"C:\Users\Donal\course\Python_labs_Mar_2025\trainer_demos\movies.txt"
fh_out = open(file, mode="wt")

# ITERATE through movies dict and WRITE key+values to FILE.
for name in movies.keys():
    print(f"{name}: {movies[name]}", end="\n", file=sys.stdout)
    print(f"{name}: {movies[name]}", end="\n", file=fh_out)
    # fh_out.write(f"{name}: {movies[name]}\n")

# fh_out.flush() # Manually flush buffers
fh_out.close() # Flush buffers and close file handle.

print("-" * 60)

# Open File handle for READING in TEXT mode
fh_in = open(file, mode="rt")

# text = fh_in.read() # Read ENTIRE file into str object! Careful of LARGE files!
# text = fh_in.read(30) # Read NEXT 30 chars into str.
# text = fh_in.readline() # Read NEXTLINE into str.
# lines = fh_in.readlines() # Read ENTIRE file into LIST object. Careful of LARGE files!
# print(f"Last line is {lines[-1]}")

# ITERATE through filehandle ONE line at a time..
# Using an ITERATOR for loop plus FileHandle (ITERATOR object iter()/next())
# for line in open(file, mode="rt"):
for line in fh_in:
    print(line, end="")
fh_in.close()
