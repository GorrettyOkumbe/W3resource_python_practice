#!/usr/bin/python3
"""finds squares of elements of a list and splits the list"""


def squares_splicing(my_list=[]):
    return [x ** 2 for x in my_list][0:5] + [x ** 2 for x in my_list][24:]
"""
squared_list = []
for x in my_list:
    squared_list +=  [x ** 2]
    a = squared_list[0:5]
    b = squared_list[24:]
    return a + b

"""


print(squares_split(range(1, 31)))
