#!/usr/bin/python3
"""class_namespace"""

import sys
import json


class Employee:
    """ my employee class"""

    count = 0
    def __init__(self, name, age, args=[]):
        self.name = name
        self.age = age
        self.args = sys.argv[1:]
        try:
            self.email = self.args[0]
            self.salary = self.args[1]
        except Exception as e:
            print("number of args is insufficient")

        Employee.count += 1
employee = Employee("sam", 34)
employee =Employee("mary",26)
#print(Employee.count)
print(Employee.__dict__)
#print(employee.salary)

