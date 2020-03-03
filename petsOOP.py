

class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs


class Dog:
    def __init__(self, color, name, age, isVaccinated):
        self.color = color
        self.name = name
        self.age = age
        self.isVaccinated = isVaccinated

    def bark(self, barkingSound):
        self.barkingSound = barkingSound

    def eat(self, food):
        self.food = food


class GermanShepherd(Dog):
    def sleep(self, sleep):
        self.sleep = sleep


class BullDog(Dog):
    def walk(self, walk):
        self.walk = walk


class Jackal(Dog):
    def dance(self, dance):
        self.dance = dance


# color = input("What's the color? ")
# name = input("What's the name? ")
# age = input("What's the age? ")
# isVaccinated = input("Is the dog vaccinated? True or False?").lower()
# sleep = "It sleeps for 5 hours"

color = "brown"
name = "rex"
age = "4 months"
isVaccinated = True
sleep = "It sleeps for 5 hours"

germanShepherd = Dog(color, name, age, isVaccinated)
print(germanShepherd.color, germanShepherd.name,
      germanShepherd.age, germanShepherd.isVaccinated)

bullDog = Dog(color, name, age, isVaccinated)
print(bullDog.color, bullDog.name,
      bullDog.age, bullDog.isVaccinated)

jackal = Dog(color, name, age, isVaccinated)
print(jackal.color, jackal.name,
      jackal.age, jackal.isVaccinated)

myDogsList = [germanShepherd, bullDog, jackal]
myPets = Pets(myDogsList)

for s in myPets.dogs:
    print("\nMy list of dogs: German Shepherd:{}, Bulldog:{},Jackal:{} ".format(
        s.name, s.color, s.age))
