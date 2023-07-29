class Card:
    def __init__(self, name, value) -> None:
        self.__name = name
        self.__value = value

    def __str__(self) -> str:
        return f"Name: {self.__name} Value: {self.__value}"
    
    def __repr__(self) -> str:
        return f"{self.__name} {self.__value}"


if __name__ == "__main__":
    card1 = Card("Club Jack", 10)
    print(card1)