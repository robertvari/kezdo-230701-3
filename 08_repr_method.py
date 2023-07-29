class Person:
    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address

    def __str__(self) -> str:
        return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}"
    
    def __repr__(self) -> str:
        return self.name

csaba = Person("Kiss Csaba", "csaba@gmail.com", "Budapest")
kriszta = Person("Nagy Krisztina", "kriszta@gmail.com", "Pécs")
tamas = Person("Kovács Tamás", "tamas@gmail.com", "Szeged")

my_friends = [csaba, kriszta, tamas]
print(my_friends)
print(my_friends[0])