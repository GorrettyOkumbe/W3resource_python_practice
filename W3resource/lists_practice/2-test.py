#!/usr/bin/python3
"""converts a list to dict
sorts keys in ascending order
strings in order of their len
return dictionary"""

def converlist_to_dict(my_list):
    if not isinstance(my_list, list):
        raise TypeError("my_list must be a list")
    my_list1 = []
    my_list2 = []
    for i in my_list:
        if isinstance(i, str):
            my_list1.append(i)
    for i in my_list:
        if isinstance(i, (int, bool)):
            my_list2.append(i)
    return my_list1 + my_list2


print(converlist_to_dict( ["Joy", "Bryan", "Mary", "Vitamax", "Dainah", 3, -15, 20, True, False]
    ))
