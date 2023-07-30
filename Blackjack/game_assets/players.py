import random

class Player_BASE:
    def __init__(self) -> None:
        self.__name = None
        self.__credits = random.randint(50, 100)
        self.__hand = []
        self.__playing = True

        self.__create()

    def __create(self):
        print("__create called")

    def __get_random_name(self):
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]

    def say_hello(self):
        print(f"Hello my name is {self.__name}")


class Player(Player_BASE):
    pass


class AIPlayer(Player_BASE):
    pass


if __name__ == "__main__":
    player = Player()
    ai_Player = AIPlayer()

    player.say_hello()
    ai_Player.say_hello()