class Dice:
    # Class attributes
    sides = 6
    color = "white"

# an instance of Dice class
dice6 = Dice()
dice10 = Dice()
dice10.sides = 10
dice10.color = "Red"

class Person:
    name = "Robert"

robert = Person()

csaba = Person()
csaba.name = "Csaba"

kriszta = Person()
kriszta.name = "Kriszta"

print(robert.name)
print(csaba.name)
print(kriszta.name)