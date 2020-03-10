from studentClass import Student
from subjectClass import Subject
from schoolClass import School
from gradingFunctions import getGrade
from gradingFunctions import getMeanScore

noOfStudents = int(input("How many students would you like to enter? "))

# input details for multiple students
for s in range(noOfStudents):
    students = []

    name = input("Enter student name: ")
    regNo = input("Enter the reg no: ")

    schoolName = input("Enter the student's school name: ")
    address = input("Enter the school's address: ")
    school = School(schoolName, address)

    # input subject details
    noOfSubjects = int(input("How many subjects would you like to enter? "))
    # input many subjects
    for s in range(noOfSubjects):
        subjects = []

        subjectName = input("Enter subject name: ")
        score = int(input("Enter the score: "))
        # Subject is an object. Create an instance of a Subject then append to subjects list
        subject = Subject(subjectName, score)
        subjects.append(subject)

    # Student is an object. Create an instance of a Student then append to students list
    student = Student(name, regNo, school, subjects)
    students.append(student)


# output student details
for s in students:
    print("\n {}, {}, {}".format(
        s.name, s.regNo, s.school.schoolName))

    for s in subjects:
        print("\n {} {} {}".format(
            s.subjectName, s.score, getGrade(score)))

    for s in subjects:
        print("Mean Grade: {}".format(getGrade(getMeanScore(score))))
    print("+"*50)
