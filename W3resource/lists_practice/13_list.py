#!/usr/bin/python3
"""program to generate a 3*4*6 3D array whose each element is *"""

def my_3D_array(x, y, z):
    """volume of a cuboid in form of *"""
    """"
    for i in range(x):
        my_list.append([])
        for j in range(y):
            my_list[i].append([])
            for k in range(z):
                my_list[i][j].append("*")
"""

    print([[["*" for k in range(z)] for j in range(y)] for i in range(x)])

print(my_3D_array(3, 4, 6))
