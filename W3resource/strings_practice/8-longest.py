#!/usr/bin/env python3
"""finds the longest string and its length"""


def length(my_list):
    """find length of elements"""
    len_str = [(x, len(x)) for x in my_list]

    for x in range(len(len_str)):
        for y in range(x + 1, len(len_str)):
            if len_str[x][1] > len_str[y][1]:
                len_str[x], len_str[y] = len_str[y], len_str[x]
    return len_str[-1][0], len_str[-1][1]


my_list = ['Mary', 'Careen', 'Elephant', 'Ann']

print(length(my_list))
