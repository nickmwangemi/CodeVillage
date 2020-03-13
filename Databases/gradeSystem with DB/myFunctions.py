import mysql.connector
from schoolClass import School
from subjectClass import Subject


def Connection():
    dbConnection = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        passwd="",
        database="grade_system_db"
    )
    return dbConnection


# create a school
def insertSchool(school):
    dbConnection = Connection()
    sql = "INSERT INTO Schools(code,name, address) VALUES (%s, %s,%s)"
    val = (school.code, school.schoolName, school.address)
    mycursor = dbConnection.cursor()
    mycursor.execute(sql, val)
    dbConnection.commit()
    print(mycursor.rowcount, "record inserted.")

    # # fetch inserted shool to get id
    sqlSelect = "SELECT * FROM Schools where code=%s"
    val = (school.code,)
    mycursor.execute(sqlSelect, val)
    insertedSchool = mycursor.fetchone()
    print(insertedSchool)
    for schl in insertedSchool:
        print(schl)

    return insertedSchool[0]


# find school by code


# create student
def insertStudent(student):
    dbConnection = Connection()
    sql = "INSERT INTO Students(name,regNo,school,subjects) VALUES (%s,%s,%s,%s)"
    val = (student.name, student.regNo, student.school.id, student.school.id)
    mycursor = dbConnection.cursor()
    mycursor.execute(sql, val)
    dbConnection.commit()
    print(mycursor.rowcount, "record inserted.")

    # fetch inserted shool to get id
    sqlSelect = "SELECT * FROM Students WHERE regNo=%s"
    val = (student.regNo,)
    mycursor.execute(sqlSelect, val)
    insertedStudent = mycursor.fetchone()
    print(insertedStudent)
    for stdnt in insertedStudent:
        print(stdnt)

    # insert subjects
    print(student.subjects)
    insertSubject(student.subjects, insertedStudent[0])

    return insertedStudent[0]

# find student by reg no

# create a subject


def insertSubject(subjects, studentId):
    dbConnection = Connection()
    for subj in subjects:
        sql = "INSERT INTO Subjects(subjectName,score,student_id) VALUES (%s,%s,%s)"
        val = (subj.subjectName, subj.score, studentId)
        mycursor = dbConnection.cursor()
        mycursor.execute(sql, val)
        dbConnection.commit()
        print(mycursor.rowcount, "subject record inserted.")


def getGrade(score):
    if score >= 80 and score <= 100:
        return 'A'
    elif score >= 60 and score < 80:
        return 'B'
    elif score >= 40 and score < 60:
        return 'C'
    elif score >= 0 and score < 40:
        return 'D'
    else:
        'Unknown Grade'


def getMeanScore(score):
    return score/3


def getSum(a, b, c):
    return a+b+c
