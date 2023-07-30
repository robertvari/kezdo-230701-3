import random, time

class Player_BASE:
    def __init__(self) -> None:
        self.__name = None
        self.__credits = 0
        self.__hand = []
        self.__playing = True

        self._create()

    @property
    def hand(self):
        return str(self.__hand)

    @property
    def playing(self):
        return self.__playing
    
    @playing.setter
    def playing(self, new_playing):
        self.__playing = new_playing

    @property
    def credits(self):
        return self.__credits

    def give_bet(self, min_bet) -> 0:
        if self.__credits < min_bet:
            self.__playing = False
            print(f"{self.name} has no more credits. :(")
            return 0
        
        return_credits = min_bet
        
        if self.hand_value >= 18 and self.hand_value < 21:
            return_credits += (self.__credits - min_bet) // 2

        if self.hand_value == 21:
            return_credits = self.__credits
        
        self.__credits -= return_credits
        print(f"{self.name} gives {return_credits} bet.")
        return return_credits

    @property
    def hand_value(self):
        return sum([card.value for card in self.__hand])

    def init_hand(self, deck):
        self.__hand.clear()
        self.__playing = True

        self.__hand.append(deck.draw())
        self._add_card(deck.draw())

    def draw_cards(self, deck):
        assert len(self.__hand) == 2, "Player hand must be inited"

        if not self.__playing:
            print(f"{self.name} not playing this time")
            return

        time.sleep(2)

        while self.__playing:
            # get hand value
            if self.hand_value < random.randint(16, 19):
                print(f"{self.name} draws a card")
                new_card = deck.draw()
                self._add_card(new_card)
            else:
                print(f"{self.name} finishes his/her turn")
                time.sleep(2)
                self.__playing = False

    def _add_card(self, new_card):
        if self.hand_value > 10 and new_card.value == 11:
            new_card.change_value()
        
        self.__hand.append(new_card)

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
        print(f"Hand Value: {self.hand_value}")

    def __repr__(self) -> str:
        return self.__name

class Player(Player_BASE):
    def _create(self):
        super()._create()
        self.name = "Robert Vari"     

    def give_bet(self, min_bet) -> 0:
        if self.credits < min_bet:
            self.playing = False
            print(f"You have no more credits. :(")
            return 0
        
        return_credits = min_bet
        print(f"The minimum bet is: {min_bet}")
        print(f"Your hand: {self.hand}")
        print(f"Hand value: {self.hand_value}")
        print(f"Your credits: {self.credits}")

        response = input("Do you want to raise? (y/n)")
        if response == "y":
            response = int(input("How much?"))
            while response > self.credits:
                print("You don't hanve enough credits.")
                response = int(input("How much?"))

            return_credits = response

        self.credits = self.credits - return_credits
        return return_credits

    def draw_cards(self, deck):
        print(f"This is your turn {self.name}")

        while self.playing:
            print(f"Your cards: {self.hand}")
            print(f"Hand value: {self.hand_value}")

            if self.hand_value >= 20:
                self.playing = False
                print(f"You finished your turn. Your hand value: {self.hand_value}")
                break
            
            response = input("Do you want to draw a card? (y/n)")
            if response == "y":
                new_card = deck.draw()
                print(f"You card: {new_card}")
                self._add_card(new_card)
            else:
                if self.hand_value < 16:
                    print(f"You have to draw a card. Your hand value is too low: {self.hand_value}")
                else:
                    self.playing = False

class AIPlayer(Player_BASE):
    pass


if __name__ == "__main__":
    from cards import Deck

    deck = Deck()
    player = Player()
    ai_player = AIPlayer()

    reward = 0
    min_bet = 10

    player.init_hand(deck)
    reward += player.give_bet(min_bet)

    ai_player.init_hand(deck)
    reward += ai_player.give_bet(min_bet)


    player.draw_cards(deck)
    ai_player.draw_cards(deck)

    player.report()
    ai_player.report()
    print(f"Reward: {reward}")
