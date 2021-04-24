from datetime import date

class Shark:

    def __init__(self, name, species, shift, food):
        self.id = ""
        self.name = name
        self.species=species
        self.shift = shift
        self.food = food
        self.status = date.today()
        self.slithering = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"