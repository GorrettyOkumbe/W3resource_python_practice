#!/usr/bin/python3

my_string = "ronny"
prac = {}
for x in my_string:
    if x in prac:
        prac[x]+= 1
    else:
        prac[x] = 1
print(prac)
