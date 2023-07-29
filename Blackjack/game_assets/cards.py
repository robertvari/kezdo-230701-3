class Card:
    def __init__(self, name, value) -> None:
        self.__name = name
        self.__value = value

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

        names = ["Heart", "Club", "Diamond", "Spade"]
    
    @property
    def cards(self):
        return str(self.__cards)


if __name__ == "__main__":
    deck = Deck()
    print(deck.cards)