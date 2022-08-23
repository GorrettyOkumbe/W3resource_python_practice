#!/usr/bin/python3
"""module to calculate the length of a string"""


def string_len_calc(my_string):
    counter = 0
    if not isinstance(my_string, str):
        raise TypeError("my_string must be a string")
    for i in my_string:
        counter += 1
    return counter
