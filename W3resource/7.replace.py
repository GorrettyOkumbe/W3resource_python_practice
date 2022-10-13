#!/usr/bin/python3

"""module for question 7 """

"""Sample String :'The lyrics is not that poor!'
                  'The lyrics is poor!'
   Expected Result:'The lyrics is good!'
                    'The lyrics is poor!'"""

"""converting not poor to good """
def replace (my_string):

    if not isinstance(my_string, str):
        raise Typeerror("my string must be a string")
    snot = my_string.find('not')
    spoor = my_string.find('poor')

    if spoor > snot and snot>0 and spoor>0:
        my_string = my_string.replace(my_string[snot:(spoor +4)], 'good')
        return my_string
    else:
        return my_string
print(replace('The lyrics is a very beautiful poem!'))
print(replace('The lyrics is poor!'))
