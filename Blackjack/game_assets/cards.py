import random


class Card:
    def __init__(self, name, value) -> None:
        self.__name = name
        self.__value = value
    
    @property
    def value(self):
        return self.__value
    
    def change_value(self):
        if self.__value == 11:
            self.__value = 1

    def __str__(self) -> str:
        return f"Name: {self.__name} Value: {self.__value}"
    
    def __repr__(self) -> str:
        return f"{self.__name} {self.__value}"


class Deck:
    def __init__(self) -> None:
        self.__cards = []
        self.create()
    
    def create(self):
        self.__cards.clear()

        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        suits = ["Heart", "Club", "Diamond", "Spade"]

        for suit in suits:
            for card_data in cards:
                card_name = f"{suit} {card_data[0]}"
                card_value = card_data[1]
                new_card = Card(card_name, card_value)
                self.__cards.append(new_card)

        random.shuffle(self.__cards)
    
    def draw(self):
        return self.__cards.pop(0)

    def show_cards(self):
        print(self.__cards)

    @property
    def card_count(self):
        return len(self.__cards)


if __name__ == "__main__":
    card1 = Card("Ace", 11)
    card2 = Card("King", 10)

    card1.change_value()
    card2.change_value()
    print(card1.value, card2.value)