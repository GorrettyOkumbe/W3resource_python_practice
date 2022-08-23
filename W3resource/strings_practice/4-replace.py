#!/usr/bin/python3

def replace(my_string=""):
    output = ""

    for x in my_string[1:]:
        if x == my_string[0]:
            x = "$"
        output += x

    return my_string[0] + output


print(replace("restart"))
