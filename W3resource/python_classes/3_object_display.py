#!/usr/bin/python3

import sys
import json
"""class_namespace"""


class Employee:
    count = 0
    #args = sys.argv
    def __init__(self, employee_name, employee_age):
        self.name = employee_name
        self.age = employee_age
        Employee.count += 1

n = len(sys.argv)
for x in range(1, n):
    print(sys.argv[x])


#print(Employee.count)
