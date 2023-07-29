import os, platform
from game_assets.cards import Deck


class Blackjack:
    def __init__(self) -> None:
        self.clear_screen()
        self.intro()

        # create a deck of cards
        self.__deck = Deck()

    def intro(self):
        print("-"*50, "BLACKJACK GAME", "-"*50)

    # protected method
    def clear_screen(self):
        os.system("cls") if platform.system() == "Windows" else os.system("clear")
    
Blackjack()