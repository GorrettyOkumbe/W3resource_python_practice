#!/usr/bin/python3
"""8-lst module"""


def empty_or_not(a=[]):
    return "Empty" if len(a) == 0 else "Not Empty"


print(empty_or_not([8, 19, 12]))
