#!/usr/bin/python3

class Student:
   student_name = "careen Naitore"
   student_id  = 90
setattr(Student, 'student_class', 'Alx cohort 5') 

   def display():
       print(f"Student name:{getattr(Student, 'student_name')}\nStudent Id:{getattr(Student, 'student_id')}\nStudent class:{getattr(Student, 'student_class')}")

    Student.display()



