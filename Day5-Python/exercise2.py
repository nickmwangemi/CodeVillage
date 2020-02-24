studentName = input("Please enter your name: ")
regNumber = input("Please enter your registration number: ")
print('=' * 50)             # print a line after user input

mathScore = int(input("Enter your score in Maths: "))
engScore = int(input("Enter your score in English: "))
kisScore = int(input("Enter your score in Kiswahili: "))


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


print('=' * 50)  # print line before report card


def getMeanScore(score):
    return score/3


def totalScore(mathScore, engScore, kisScore):
    return mathScore + engScore + kisScore


# print report card
print('Exam Report for: {} Reg. No.{}'.format(studentName, regNumber))
print('MATH: {}'.format(checkGrade(mathScore)))
print('ENG: {}'.format(checkGrade(engScore)))
print('KIS: {}'.format(checkGrade(kisScore)))
print('Total Score: {}'.format(totalScore(mathScore, engScore, kisScore)))
print('Mean Grade: {}'.format(checkGrade(
    getMeanScore(totalScore(mathScore, engScore, kisScore)))))
