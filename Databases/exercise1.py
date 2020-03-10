import mysql.connector
mydbConnection = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root",
    passwd="",
    database="my_schools_db"
)

cursor = mydbConnection.cursor()
cursor.execute("SELECT * FROM schools")
schools = cursor.fetchall()
for sch in schools:
    print(sch)
