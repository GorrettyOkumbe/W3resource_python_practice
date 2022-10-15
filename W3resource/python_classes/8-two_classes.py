#!/usr/bin/python3
"""creating two classes in a module"""

class Student:
    pass

class Marks:
    pass

print(type(Student))
print(type(Marks))

student1 = Student()
marks1 = Marks()

print(type(student1))
print(isinstance(student1, Student))
print(isinstance(student1, Marks))
print(type(marks1))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))

"""checks if class is a subclass of object"""
print(issubclass(Student, object))
print(issubclass(Marks, object))
