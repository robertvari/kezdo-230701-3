class Student:
    def __init__(self, first_name, last_name) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__scores = []
    
    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"
    
    @property
    def scores(self):
        return self.__scores
    
    def set_score(self, new_score):
        self.__scores.append(new_score)

    @property
    def average(self):
        return sum(self.__scores) / len(self.__scores)
    
    def __str__(self) -> str:
        return f"{self.__first_name} {self.__last_name}"

csaba = Student("Kiss", "Csaba")
csaba.set_score(5)
csaba.set_score(2)
csaba.set_score(3)
csaba.set_score(1)
print(csaba.full_name, csaba.average)