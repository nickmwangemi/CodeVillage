# multiple students
students = dict()

# no of students
noOfStudents = int(input("Enter the number of students:  "))


def getGrade(score):
    if(score >= 80 and score <= 100):
        return "A"
    elif(score >= 60 and score < 80):
        return "B"
    elif(score >= 40 and score <= 60):
        return "C"
    elif (score >= 0 and score < 40):
        return "D"
    else:
        'Unknown Grade'


def getMeanScore(score, noOfSubjects):
    return totalMarks/noOfSubjects


def getSchoolMeanScore(totalClassMarks, noOfStudents):
    return totalClassMarks / noOfStudents


# input details for many students
for n in range(1, noOfStudents+1):
    student = dict()
    studentName = input("Enter Student Name: \n")
    regNo = input("Enter Registration Number: \n")
    studentClass = input("Enter the Student's Class: \n")
    student['name'] = studentName
    student['regNo'] = regNo
    student['class'] = studentClass
    noOfSubjects = int(input("Enter number of subjects: "))
    subjects = dict()

    for s in range(1, noOfSubjects+1):
        subjectName = input("Enter the name of the subject: \n".strip())
        subjectScore = int(
            input("Enter the score for {} \n".format(subjectName)))
        subjects[subjectName] = subjectScore

    student['scores'] = subjects
    students[regNo] = student

print("*"*10, "Report Card", "*"*10)
for key, value in students.items():
    print("\nName: ", value['name'])
    print("Reg No: ", value['regNo'])
    print("Class: ", value['class'])
    totalMarks = 0

    for subject, score in value['scores'].items():
        totalMarks += score
        print(subject, score, getGrade(score))

    print("MEAN SCORE: ", getMeanScore(totalMarks, len(value['scores'])))
    print("MEAN GRADE: ", getGrade(
        getMeanScore(totalMarks, len(value['scores']))))

    totalClassMarks = 0
    for student, score in value['scores'].items():

        # school mean score
    print("SCHOOL MEAN SCORE: ", getSchoolMeanScore(
        totalClassMarks, noOfStudents))
    # school mean grade
    print("SCHOOL MEAN GRADE: ")


print("*"*10, "End of Report Card", "*"*10)
