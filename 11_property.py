class Dice:
    allowed_colors = ["white", "red", "green", "blue"]
    allowed_sides = [6, 12, 20]

    def __init__(self, sides, color) -> None:
        self.__sides = sides
        self.__color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, new_color):
        self.__color = new_color
    
    @property
    def sides(self):
        return self.__sides

    @sides.setter
    def sides(self, new_sides):
        self.__sides = new_sides

    def __str__(self) -> str:
        return f"Sides: {self.__sides} Color: {self.__color}"
    
dice6 = Dice(6, "white")
dice6.color = "Red"
print(dice6)