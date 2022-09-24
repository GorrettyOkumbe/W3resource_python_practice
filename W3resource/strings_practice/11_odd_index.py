#!/usr/bin/python3
"""odd numbex index"""

def odd_ind(my_string):
    """checks and removes the odd number value indexes"""
    var1 = ""
    for x in range(len(my_string)):
        if x % 2 == 0:
            var1 += my_string[x]
    return var1

print(odd_ind("python"))

