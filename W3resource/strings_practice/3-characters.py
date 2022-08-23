#!/usr/bin/python3
"""first and last two characters of a string"""

import len_str as mod


def string_characters(x=""):
    my_string = x

    counter = mod.string_len_calc(x)
    if counter < 2:
        return ""
    if counter == 2:
        return my_string * 2

    else:
        return my_string[0:2] + my_string[-2:]


print(string_characters("a"))
