#!/usr/bin/python3

def sorting_list(my_list):
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] < my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    return my_list


print(sorting_list([12, -5, 0.99, 97, 3, -0.99, 1]))
