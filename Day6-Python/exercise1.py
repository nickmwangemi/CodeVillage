# loops
students = dict()
students['1'] = 'Peter'
students['2'] = 'Brian'
students['3'] = 'Nick'

for a in students:
    print(students[a])

# .values()
for v in students.values():
    print(v)

# .items()
for key, values in students.items():
    print(key, values)

# len()
print(len(students))

# .clear()
students.clear()
print(len(students))

# .pop() - removes last item
students.pop()

# .del()
del students['1']
