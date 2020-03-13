# Best practice to mitigate SQL injections
from connectionFunction import Connection

mydbConnection = Connection()
cursor = mydbConnection.cursor()

sql = "INSERT INTO schools(code,name,address) values( %s, %s, %s)"
myValues = ('2003', 'Bungoma Boys High Sch', 'Bungoma')

cursor.execute(sql, myValues)
mydbConnection.commit()

cursor.execute("SELECT * from schools")
schools = cursor.fetchall()
for sch in schools:
    print(sch)
