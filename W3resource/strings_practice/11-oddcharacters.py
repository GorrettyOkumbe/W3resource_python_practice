#!/usr/bin/python3

""" remove the character at the odd
    index in a string:
    input: "python"
    output: "pto"
"""


def odd_character(my_string):
    # checks if it is a string
    if not isinstance(my_string, str):
        raise Typerror("my_string is not a string")
    string2 = ""
    for c in range(len(my_string)):
        if c % 2 == 1:
            continue
        string2 += my_string[c]
    return string2


print(odd_character("python"))
