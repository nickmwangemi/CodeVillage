import mysql.connector


def Connection():
    mydbConnection = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        passwd="",
        database="my_schools_db"
    )
    return mydbConnection
