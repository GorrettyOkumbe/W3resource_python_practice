#!/usr/bin/python3
# use the command
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def swap (st1, st2):
    # checks if it is a string
    if not isinstance (st1, str):
        raise Typerror("my string is not a string")
    mystring1 = ""
    mystring2 = ""
    for s in st1[:2]:
        mystring1 += s
    for t in st2[:2]:
        mystring2 += t
    return mystring2+st1[-1] +" "+ mystring1+st2[-1]



print(swap('abc' , 'xyz'))

