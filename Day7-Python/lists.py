students = []
students = ['Kim', 'Brian', 'James', 'Peter', 'John', 'Kim']
studentsCopy = students[:]

print(students[-2])
print(studentsCopy)

# don't need to know length of the list
for n in students:
    print(n)

# need to know the length of the list
for n in range(0, len(students)):
    print(n)
    print(students[n])


students[0] = 'Kimani'
print(students)
print(students[:])
