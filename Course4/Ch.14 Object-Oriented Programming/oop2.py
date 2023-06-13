class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, name):
        self.name = name
        print(f"{self.name} constructed")

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points += 7
        self.party()
        print(f"{self.name} points {self.points}")


s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
