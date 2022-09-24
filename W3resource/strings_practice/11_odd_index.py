#!/usr/bin/python3

def odd_ind(str):
    var1 = ""
    for x in range(len(str)):
        if x % 2 == 0:
            var1 += str[x]
    return var1

print(odd_ind("python"))

