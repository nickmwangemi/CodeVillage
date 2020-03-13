from connectionFunction import Connection

mydbConnection = Connection()
cursor = mydbConnection.cursor()
# cursor.execute(
#     "INSERT INTO schools(code, name, address)  values('2000', 'Mumias High Sch', 'Mumias');")

cursor.execute(
    "INSERT INTO schools(code, name, address)  values('2001', 'Butere High Sch', 'Mumias');")
mydbConnection.commit()

cursor.execute("SELECT * from schools")
schools = cursor.fetchall()
for sch in schools:
    print(sch)
