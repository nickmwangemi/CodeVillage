from connectionFunction import Connection

mydbConnection = Connection()
cursor = mydbConnection.cursor()
cursor.execute("SELECT * FROM schools")
schools = cursor.fetchall()
for sch in schools:
    print(sch)
