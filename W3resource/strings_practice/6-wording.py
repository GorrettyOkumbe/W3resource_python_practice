#!/usr/bin/python3
#Sample String : 'abc'
#Expected Result : 'abcing'
#Sample String : 'string'
#Expected Result : 'stringly'
import len_str as mod 
def swap (my_string):
    # checks if it is a string
    if not isinstance (my_string, str):
        raise Typerror("my string is not a string")
    count = mod.string_len_calc(my_string)
    if count < 3 :
        return my_string
    elif count == 3 :
        return my_string+"ing"
    elif my_string[-3:] in "ing":
        return my_string+"ly"


print(swap('st'))

