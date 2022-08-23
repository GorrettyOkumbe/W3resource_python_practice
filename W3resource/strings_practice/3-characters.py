#!/usr/bin/python3
"""first and last two characters of a string"""

counter = __import__('1-len_str').string_len_calc

def string_characters(my_string):
    if counter< 2:
        return
    elif counter == 2:
        return my_string * 2

    else:
        return my_string[0:2] + my_string[-2:]

print(string_characters("w3resource"))

