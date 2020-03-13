from schoolClass import School
from studentClass import Student
from subjectClass import Subject
from myFunctions import getGrade
from myFunctions import insertSchool
from myFunctions import insertStudent

noOfStudents = int(input('Enter the no of students: '))

students = []
# input details for many students
for n in range(1, noOfStudents+1):
    studentName = input('Enter Name of Student: ')
    regNo = input('Enter Reg Number: ')

    schoolCode = input('Enter School Code: ')
    schoolName = input('Enter Name of School: ')
    schoolAddress = input('Enter School Address: ')

    school = School(id, schoolCode, schoolName, schoolAddress)
    # insert school to a database
    schoolid = insertSchool(school)
    school.id = schoolid

    nofsubjects = int(input('Enter no. of subjects: '))
    subjects = []
    for s in range(1, nofsubjects+1):
        subjectName = input('Enter name of Subject: ')
        subjectSCore = int(
            input('Enter the score for {}: '.format(subjectName)))
        subject = Subject(subjectName, subjectSCore)
        subjects.append(subject)
        # insert subject to database

    student = Student(studentName, regNo, school, subjects)
    students.append(student)
    # insert student to database
    studentid = insertStudent(student)


for stdnt in students:
    print(stdnt.name, stdnt.school.schoolName, len(stdnt.subjects))
    for subject in subjects:
        print(subject.subjectName, ':', subject.score,
              'Grade : ', getGrade(subject.score))
