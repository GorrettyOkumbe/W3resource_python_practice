#!/usr/bin/python3
"""practice 2 on lists module"""


def mul_list_elements(a=list):
    """multiplies elments of a list"""
    n = 1
    for i in a:
        n = n * i
    return n


print(mul_list_elements(a=[2, 3, 4]))
