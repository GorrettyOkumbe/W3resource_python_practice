#!/usr/bin/python3
"""sorting a list module"""


def sortinglist(my_list=[]) -> list:
    """sorts list elements in ascending order"""
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i][1] > my_list[j][1]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    print(my_list)


# print(sortinglist([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
sortinglist([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
print(sortinglist.__annotations__)
