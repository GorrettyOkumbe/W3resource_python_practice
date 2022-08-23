#!/usr/bin/python3
"""practice  on lists module"""


def min_list_elements(a=list):
    a_min = a[0]
    for x in a:
        if x <= a_min:
            a_min = x
    return a_min


print(min_list_elements(a=[2, 3, 0, 4, 5]))
