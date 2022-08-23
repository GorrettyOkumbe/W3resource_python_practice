#!/usr/bin/python3
"""11-intersection module"""


def intersection(a=[], b=[]):
    """checks if there is atleast a common number in the lists
    return: True or false"""
    for x in a:
        for y in b:
            if x in b or y in a:
                return True
        return False

print(intersection([2, 8, 14, 27], [5, 27, 5, 3]))
