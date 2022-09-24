#!/usr/bin/python3

def odd_ind(my_string):
    var1 = ""
    for x in range(len(my_string)):
        if x % 2 == 0:
            var1 += my_string[x]
    return var1

print(odd_ind("python"))

