# get names of students
noOfStudents = int(input("How many students are you adding? "))
print("+"*50)


# store in a set
students = set([])

# loop through set to add items to set
for s in range(noOfStudents):
    name = input("Enter student name: ")
    students.add(name)

print("+"*50)

print("This is your list of students:")
for n in students:
    print("\t{}".format(n))
