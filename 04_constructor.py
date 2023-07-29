class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

robert = Person("Robert", "robert@gmail.com")
kriszta = Person("Kriszta", "krisztagmail.com")
csaba = Person("Csaba", "csaba@gmail.com")

print(robert.name)
print(kriszta.name)
print(csaba.email)