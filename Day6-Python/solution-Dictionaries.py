numOfStudents = int(input("Please enter number of students: "))
print("You entered {} student(s)".format(numOfStudents))
print("*"*50)
studentInfo = {}

studentData = []
for i in range(0, numOfStudents):
    studentName = input("Enter student name: ")
    studentInfo[studentName] = {}

    regNo = input("Enter Registration Number: ")
    studentInfo[regNo] = {}

    studentClass = input("Enter the Student's Class: ")
    studentInfo[studentClass] = {}

    for entry in studentData:
        # storing the marks entered as integers to perform arithmetic operations later on.
        studentInfo[studentName][entry] = int(input(entry))


# print studentInfo
print("*"*50)
print("Please enter student name to get their report card")
name = input("Student name: ")

if name in studentInfo.keys():
    print("Average Score: ", str(sum(studentInfo[name].values())/3.0))
    print("Total Score: ", str(sum(studentInfo[name].values())))  # total score
    print("")  # grade for each subject
    print("")  # mean grade
    print("")  # school mean score
    print("")  # school mean grade

else:
    print("please enter valid name")
