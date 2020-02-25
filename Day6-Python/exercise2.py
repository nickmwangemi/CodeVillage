"""
enter no of subjects
enter no of students
for each student:
  - Capture - reg
            - class
            - name
            - subject and scores
output:
 - grade for each student
 -mean grade
 - school meanscore
 - school meangrade
"""


print("=====WELCOME=============")
print("Record student test scores here")
numOfStudents = int(
    input("Please enter number of students you wish to enter:"))
print("You are entering {} students".format(numOfStudents))


studentInfo = dict()

studentData = dict()
for i in range(0, numOfStudents):
    studentName = input("Enter Student Name :")
    numOfSubjects = int(input("Please enter the number of subjects"))
    studentInfo[studentName] = {}
    for entry in studentData:
        # storing the marks entered as integers to perform arithmetic operations later on.
        studentInfo[studentName][entry] = int(input(entry))
# print studentInfo
