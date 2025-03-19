#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO create, and grow, and shrink
# dictionaries (Unordered collection with Unique keys).
# From Python 3.6, dict keys+values are ordered in insertion order.
"""
    Docstring:
"""
import pprint

# Example of a multi-dimensional dict of lists.
movies = { 'rohit': ['internal affairs', 'inside out', 'death at a funeral'],
           'david': ['borat', 'grimsby', 'dictator'],
           'donald': ['lotr', 'the hobbit', 'brave']
}

# Grow dictionary..
movies['isla'] = ['avengers', 'winter soldier', 'age of ultron']
movies['grace'] = ['top gun', 'braveheart', 'babe']

# Shrink a dictionary..
movies.pop('david') # Pop/remove key+value
movies.popitem() # Pop/removes last INSERTED key+value

# films = movies.copy() # Copy dictionary
# films.clear() # Empty dictionary

# Access keys and values..
print(f"Isla's favourite movies are {movies['isla']}")
print(f"Isla's favourite movies are {movies.get('isla')}")
print(f"Rohit's ultimate movie is {movies['rohit'][0]}")

# pprint.pprint(movies)
print("-" * 60)

# But its common to ITERATE through the keys using .keys() method
for name in movies.keys():
    print(f"{name} likes {movies[name]}")

# But its common to ITERATE through the values using .values() method
for films in movies.values():
    print(f"Good films = {films}")

# But its common to ITERATE through the BOTH keys+values using .items() method
for (name, films) in movies.items():
    print(f"{name} LOVES the films {films}")
















