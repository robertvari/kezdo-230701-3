class Person:
    # class attribute
    race = "human"

    def __init__(self, name):
        # instance attribute
        self.name = name

class Dog:
    # class attribute
    race = "animal"

    def __init__(self, name):
        # instance attribute
        self.name = name


csaba = Person("Csaba")
my_pet = Dog("Rex")
print(csaba.name, Person.race)
print(my_pet.name, Dog.race)