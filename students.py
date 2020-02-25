noOfStudents = int(input("Enter the number of students:  "))

studentSubjects = []
studentScore = []
studentName = []
for s in range(noOfStudents):
    regNumber = (input("Enter registration number: "))
    studentclass = input("Enter student class: ")
    name = input("Enter student name: ")
    noOfSubjects = int(input("Enter number of subjects you want to add: "))

    for j in range(noOfSubjects):
        subject = input("Enter subject: ")
        studentSubjects.append(subject)
        score = int(input("Enter score: "))
        studentScore.append(score)
        studentName.append(name)


def checkGrade(score):
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


print("*" * 50)  # print line before report card


def getMeanScore(score):
    return score/noOfSubjects


def totalScore(score):
    return sum(studentScore)


# print('Total Score: {}'.format(totalScore(mathScore, engScore, kisScore)))
# print('Mean Grade: {}'.format(checkGrade(getMeanScore(totalScore(mathScore, engScore, kisScore)))))

print("*"*50)
stuName = input("Please enter student name to get their report card: ")
if stuName in studentName:
    # print report card
    print('Exam Report for: {} Reg. No.{}'.format(studentName, regNumber))
    print('{} {}'.format(studentSubjects[0:-1], checkGrade(score)))
    print("Total Score: {}".format(totalScore(score)))
    print("Mean Score: {}".format(getMeanScore(score)))
