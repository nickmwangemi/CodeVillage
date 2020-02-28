# get number of students
noOfStudents = int(input("How many students are you adding? "))
print("+"*50)

# create list to store student names
students = []

# loop the user input to capture the number of students
for s in range(noOfStudents):
    name = input("Enter student name: ")
    students.append(name)

print("+"*50)

print("This is your list of students:")
for n in students:
    print("\t{}".format(n))
