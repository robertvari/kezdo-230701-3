from random import choice, randint
from time import sleep

class Person:
    def __init__(self, name) -> None:
        self.name = name
    
    def say_hello(self):
        choices = ["How are you?", "Hope you are well", "Nice to meet you", "What is your name?"]
        print(f"Hello! My name is {self.name}. {choice(choices)}")

class Dice:
    def __init__(self, sides, color) -> None:
        self.sides = sides
        self.color = color

    def roll(self):
        print(f"Dice {self.sides} is rolling...")
        sleep(randint(2,6))
        print(f"The resoult is: {randint(1, self.sides)}")

dice6 = Dice(6, "White")
dice10 = Dice(10, "Blue")
dice20 = Dice(20, "Green")
dice6.roll()
dice10.roll()
dice20.roll()