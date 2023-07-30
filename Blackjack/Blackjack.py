import os, platform
from game_assets.cards import Deck
from game_assets.players import Player, AIPlayer


class Blackjack:
    def __init__(self) -> None:
        # create a deck of cards
        self.__deck = Deck()
        self.__player = Player()
        self.__player_list = []
        self.__reward = 0
        self.__min_bet = 10

        self.clear_screen()
        self.intro()
        self.__create_player_list()
        self.__game_loop()

    def __game_loop(self):
        self.clear_screen()
        self.__deck.create()
        self.__reward = 0

        # init players
        for player in self.__player_list:
            player.init_hand(self.__deck)
            self.__reward += player.give_bet(self.__min_bet)

        # start rounds
        for player in self.__player_list:
            print("-"*50)
            player.draw_cards(self.__deck)

        self.__get_winner()

    def __get_winner(self):
        print("Get winner!!!")

    def __create_player_list(self):
        self.__player_list.append(self.__player)
        self.__player_list.append(AIPlayer())
        self.__player_list.append(AIPlayer())
        self.__player_list.append(AIPlayer())

    def intro(self):
        print("-"*50, "BLACKJACK GAME", "-"*50)

    # protected method
    def clear_screen(self):
        os.system("cls") if platform.system() == "Windows" else os.system("clear")
    
Blackjack()