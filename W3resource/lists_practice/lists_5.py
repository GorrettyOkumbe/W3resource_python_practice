#!/usr/bin/python3
"""lists_5 module"""


def palidrome_elements(a=[]):
    b = [i for i in a if len(i) >=2 and i[0] == i[len(i) - 1]]
    return len(b)

print(palidrome_elements(['abc', 'xyz', 'aba', '1221']))
