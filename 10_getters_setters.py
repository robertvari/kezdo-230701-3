class Dice:
    allowed_colors = ["white", "red", "green", "blue"]
    allowed_sides = [6, 12, 20]

    def __init__(self, sides, color) -> None:
        assert color.lower() in Dice.allowed_colors, f"Allowed colors: {Dice.allowed_colors}"
        assert sides in Dice.allowed_sides, f"Allowed sides: {Dice.allowed_sides}"

        # private attribute
        self.__sides = sides
        self.__color = color
    
    def get_sides(self):
        return self.__sides
    
    def get_color(self):
        return self.__color
    
    def set_color(self, new_color):
        assert new_color.lower() in Dice.allowed_colors, f"Allowed colors: {Dice.allowed_colors}"
        self.__color = new_color.lower()

    def __str__(self) -> str:
        return f"Sides: {self.__sides} Color: {self.__color}"
    
dice6 = Dice(6, "white")
print(dice6)