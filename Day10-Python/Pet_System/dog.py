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
