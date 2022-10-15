#!/usr/bin/python3

class Student:
    name = "careen Naitore"
    marks  = 90

print(f"Student Name:{getattr(Student, 'name')}")
print(f"Student Marks:{getattr(Student, 'marks')}")

setattr(Student, 'name', 'Rony Opunga')
setattr(Student, 'marks', '95')

print(f"Student Name:{getattr(Student, 'name')}")
print(f"Student Marks:{getattr(Student, 'marks')}")



