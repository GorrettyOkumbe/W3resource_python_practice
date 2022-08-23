#!/usr/bin/python3
"""practice  on lists module"""


def max_list_elements(a=list):
    a_max = a[0]
    for x in a:
        if x >= a_max:
            a_max = x
    return a_max


print(max_list_elements([4, 8, 3, 35, 7, 10]))
