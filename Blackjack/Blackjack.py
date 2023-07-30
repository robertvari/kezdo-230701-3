import os, platform, time
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

        time.sleep(3)
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
        time.sleep(3)
        self.clear_screen()

        winner_list = [player for player in self.__player_list if player.hand_value <= 21]

        if not winner_list:
            print("House wins")
        else:
            sorted_winnder_list = sorted(winner_list, key=lambda player: player.hand_value)
            winner = sorted_winnder_list[-1]

            winner.give_reward(self.__reward)

        response = input("Dou you want to play again? (y/n)")
        if response == "y":
            self.__game_loop()
        
        print("Good bye!")

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