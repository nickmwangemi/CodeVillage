from pet import Pets
from dog import Dog


class BullDog(Dog):
    def __init__(self, color, name, age, isVaccinated, noOfPuppies):
        super().__init__(color, name, age, isVaccinated)
        self.noOfPuppies = noOfPuppies

    def walk(self, walk):
        self.walk = walk
