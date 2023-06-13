class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, name):
        self.name = name
        print(f"{self.name} constructed")

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

    def __del__(self):
        print("I am destructed")


an = PartyAnimal('John Doe')
an.party()
an.party()
an = 42
print("an container", an)
