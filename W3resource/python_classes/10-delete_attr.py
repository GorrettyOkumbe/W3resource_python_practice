#!/usr/bin/python3

class Student:
   student_name = "careen Naitore"
   student_id  = 90

print(f"Student Name:{getattr(Student, 'student_name')}")
print(f"Student id:{getattr(Student, 'student_id')}")

setattr(Student, 'student_class', 'Alx cohort 5')

print(f"Student class:{getattr(Student, 'student_class')}")

delattr(Student, 'student_name')
print(Student.__dict__)



