#!/usr/bin/python3
# use the command
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def swap (st1, st2):
    # checks if it is a string
    if not isinstance (st1, str):
        raise Typerror("my string is not a string")
    return st2[:2]+st1[-1] +" "+ st1[:2]+st2[-1]



print(swap('abc' , 'xyz'))

