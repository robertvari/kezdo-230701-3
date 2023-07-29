class Person:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

csaba = Person("Kiss Csaba")
kriszta = Person("Nagy Krisztina")
tamas = Person("Kovács Tamás")

print(csaba)
print(kriszta)
print(tamas)