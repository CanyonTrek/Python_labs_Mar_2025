#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO preserve 1 Python object
# into a file using the pickle module.
"""
    Docstring:
"""
import pickle
import pprint
import gzip # shutil, bz2, tarfile

movies = { 'rohit': ['internal affairs', 'inside out', 'death at a funeral'],
           'david': ['borat', 'grimsby', 'dictator'],
           'donald': ['lotr', 'the hobbit', 'brave'],
           'isla': ['avengers', 'winter soldier', 'age of ultron']
}

file = r"C:\Users\Donal\course\Python_labs_Mar_2025\trainer_demos\movies.pgz"

# Open file handle for WRITING in BINARY mode
# with open(file, mode="wb") as fh_out:
with gzip.open(file, mode="wb") as fh_out:
    # pickle.dump(movies, fh_out, protocol=5) # Protocol 0=ASCII 1=5=BINARY
    # pickle.dump(movies, fh_out, pickle.DEFAULT_PROTOCOL)  # Py3.13 = 4
    pickle.dump(movies, fh_out, pickle.HIGHEST_PROTOCOL)  # Py3.13 = 5


# Open file handle for READING in BINARY mode
# with open(file, mode="rb") as fh_in:
with gzip.open(file, mode="rb") as fh_in:
    films = pickle.load(fh_in)

pprint.pprint(movies)
print("-" * 60)
pprint.pprint(films)


