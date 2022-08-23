#!/usr/bin/python3
"""use of remove method"""


def remove_from_list(a=[]):
    """removes element at specified position in a list"""

    for x in a:
        a.remove(a[0])
        a.remove(a[4])
        return a


print(remove_from_list(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))
