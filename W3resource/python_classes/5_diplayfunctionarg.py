#!/usr/bin/python3
"""Display function argument"""


def student(name, age, id):
    pass

print(__import__("inspect").getfullargspec(student))
