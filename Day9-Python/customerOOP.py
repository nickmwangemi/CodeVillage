class Customer:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def myOutput(self):
        print(self.firstname)
        print(self.lastname)
        print(self.age)


Nick = Customer("Nick", "Mwangemi", 23)
Jane = Customer("Jane", "Doe", 43)
John = Customer("John", "Doe", 23)
print(Nick.firstname, Jane.firstname, John.firstname)

Nick.myOutput()
Jane.myOutput()
John.myOutput()
