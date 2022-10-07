#!/usr/bin/python3

import array

print(dir(array))
print(array.__dict__)
for name in array.__dict__:
    print(name)
