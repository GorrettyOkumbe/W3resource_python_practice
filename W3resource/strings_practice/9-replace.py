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
        raise TypeError("my_string is not a string")
    if not isinstance (n, int):
        raise TypeError("n must be an integer")
    if n > len(my_string):
        raise ValueError("n out of range")
    string=""
    for x in range(len(my_string)):
        if x == n:
            continue
        string += my_string[x]
    return string

print(remove("python", 100))

         
