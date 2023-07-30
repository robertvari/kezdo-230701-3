import random

class Player_BASE:
    def __init__(self) -> None:
        self.__name = None
        self.__credits = 0
        self.__hand = []
        self.__playing = True

        self._create()

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def credits(self):
        return self.__credits
    
    @credits.setter
    def credits(self, new_credits):
        self.__credits = new_credits 

    def _create(self):
        self.__name = self.__get_random_name()
        self.__credits = random.randint(50, 100)

    def __get_random_name(self) -> str:
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]

        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def report(self):
        print("-"*50)
        print(f"Name: {self.__name}")
        print(f"Credits: {self.__credits}")
        print(f"Hand: {self.__hand}")
        print(f"Playing: {self.__playing}")


class Player(Player_BASE):
    def _create(self):
        super()._create()
        self.name = "Robert Vari"     


class AIPlayer(Player_BASE):
    pass


if __name__ == "__main__":
    player = Player()
    ai_Player = AIPlayer()

    player.report()
    ai_Player.report()