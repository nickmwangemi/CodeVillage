students = dict()

student1 = dict()
student1['RegNo'] = '1234'
student1['Name'] = 'Nick'

student2 = dict()
student2['RegNo'] = '5678'
student2['Name'] = 'Brian'

students['1'] = student1
students['2'] = student2

print(student1['RegNo'])
print(students)
print(students.get(1))
