class Dice:
    def __init__(self, sides, color) -> None:
        # public attributes
        # self.sides = sides
        # self.color = color

        # protected attributes
        # self._sides = sides
        # self._color = color

        # private attribute
        self.__sides = sides
        self.__color = color

    def __str__(self) -> str:
        return f"Sides: {self.__sides} Color: {self.__color}"
    
dice6 = Dice(6, "White")
print(dice6.sides)