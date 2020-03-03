# declaring a set
students = set(["Kim", "John", "Kip"])
print(students)

# to access list items, use a loop
for n in students:
    print(n)

# also..
if "Kim" in students:
    print("Kim is present")

# adding items to set
students.add("Nick")
students.add("Lucy")
print(students)

# checking length of set
print(len(students))

# adding multiple items
students.update(["Brian", "Lynn", "Pauline", "Joy"])
print(students)

# removing item from set
students.remove("John")
students.discard("Pauline")
print(students)
