#!/usr/bin/python3
"""10-find_words module"""


def find_words(my_list, n):
    """finds list of words longer than n"""
    # b = list(my_list)
    return [x for x in list(my_list) if len(x) > n]


""""
    for x in a:
        if len(x) > n:
            return a
"""
print(find_words(["mary", "Ronny", "Vitamax", "Bryan"], 4))
#!/usr/bin/python3
