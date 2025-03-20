#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO open, and close, and read, write
# and append randomly to a TEXT and binary file.
"""
    Docstring:
"""
movies = { 'rohit': ['internal affairs', 'inside out', 'death at a funeral'],
           'david': ['borat', 'grimsby', 'dictator'],
           'donald': ['lotr', 'the hobbit', 'brave'],
           'isla': ['avengers', 'winter soldier', 'age of ultron']
}

file = r"C:\Users\Donal\course\Python_labs_Mar_2025\trainer_demos\movies.txt"

# Open file handle for READING in TEXT mode
with open(file, mode="rt") as fh_in:
    fh_in.seek(90, 0) # Seek forwards 90 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() -len(text)} = {text}")

    fh_in.seek(130, 0) # Seek forwards 130 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() -len(text)} = {text}")

# Open file handle for READING in binary mode
with open(file, mode="rb") as fh_in:
    fh_in.seek(-140, 2) # Seek back 140 bytes from EOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() -len(text)} = {text}")

    fh_in.seek(-65, 1) # Seek back 45 bytes from current position
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() -len(text)} = {text}")