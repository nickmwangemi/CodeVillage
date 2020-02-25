"""
User to enter multiple subjects and scores
Option to end
Output:
    -Subject
    -Grade
    -Mean Grade
"""

noOfSubjects = int(input("Enter number of subjects: "))
subjects = dict()

for n in range(1, noOfSubjects+1):
    subjectName = input("Enter the subject name: ")
    score = int(input("Enter the score: "))
    subjects[subjectName] = score


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


for key, value in subjects.items():
    print(key, '', checkGrade(value))


print('=' * 50)  # print line before report card


def getMeanScore(score, noOfSubjects):
    return score/noOfSubjects


def totalScore(subjects):
    return sum(subjects)


print("Total Score: {}".format(totalScore(subjects)))
