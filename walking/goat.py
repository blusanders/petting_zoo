from datetime import date

class Goat:

    def __init__(self,name,species):
        self.id = ""
        self.name = name
        self.species=species
        self.status = date.today()
        self.walking = True