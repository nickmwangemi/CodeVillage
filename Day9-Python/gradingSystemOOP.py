"""
Allow user to input as many students
Store student objects in a list
Output each students details
Student has:
- Name
- reg no
- student class
"""


class Student:
    def __init__(self, name, regNo, studentClass):
        self.name = name
        self.regNo = regNo
        self.studentClass = studentClass


# multiple students
students = []
noOfStudents = int(input("How many students would you like to enter? "))

# input details for many students
for s in range(noOfStudents):
    name = input("Enter student name: ")

    regNo = input("Enter the reg no: ")

    studentClass = input("Enter the student's class: ")

    # Student is an object. Create an instance of a student then append to students list
    student = Student(name, regNo, studentClass)
    students.append(student)


# output student details
for s in students:
    print("\n Name:{} Reg.No:{} Student Class:{}".format(
        s.name, s.regNo, s.studentClass))
