#!/usr/bin/python3

"""module for question 6 """

"""Sample String : 'abc'
   Expected Result : 'abcing'
   Sample String : 'string'
   Expected Result : 'stringly'"""

""" Adding ly and ing to a string of letter """

import len_str as mod 
def swap (my_string):
    # checks if it is a string
    if not isinstance (my_string, str):
        raise Typerror("my string is not a string")
    count = mod.string_len_calc(my_string)
    if count < 3 :
        return my_string
    elif count >= 3 and my_string[-3:] not in "ing":
        return my_string+"ing"
    else:
        return my_string+"ly"


print(swap('wrapp'))

