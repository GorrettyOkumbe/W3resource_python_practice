#!/usr/bin/python3
"""calculates the character frequency in a string"""

def char_frequency(my_string):
    """returns a dictionary of char and its count"""
    if not isinstance(my_string, str):
        raise TypeError("my_string must be a string")
    return {x: my_string.count(x) for x in my_string}

print(char_frequency('google.com'))

