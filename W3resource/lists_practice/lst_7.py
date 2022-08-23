#!/usr/bin/python3
"""lst_7 module"""


def remove_duplicates(my_list=[]):
    """removes dulicates from a list"""
    new_list = []
    for x in my_list:
        if x not in new_list:
            new_list.append(x)
    return new_list


print(remove_duplicates([3, 8, 6, 9, 3, 7, 7]))
#!/usr/bin/python3
