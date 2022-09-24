#!/usr/bin/python3

""" remove the character at the nth 
    number in a string:
    input: "python"
    output: "pthon"
    n = 1
"""

def remove (my_string, n):
    # checks if it is a string
    if not isinstance (my_string, str):
        raise Typerror("my string is not a string")
    string =""
    for x, y in enumerate(my_string):
        if x != n:
            string += y
    return string

print(remove("python", 1))

         
