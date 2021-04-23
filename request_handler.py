from slithering import Anaconda
from slithering import Cobra
from swimming import Baracuda
from swimming import Shark
from walking import Goat
from walking import Pig
from attraction import PettingZoo
from attraction import SlitherInn

# print(f'{connie.name} the {connie.species} is available to pet during the {connie.shift} shift.')
# print(connie.feed())
# print(connie)

connie = Pig("Connie", "Goat", "Morning", "Apples")
bill = Goat("Bill", "Goat", "Afternoon", "Grass")
al = Anaconda("Al", "Snake", "Night", "Rats") 
sam = Shark("Sam", "Shark", "Afternoon", "Surfers") 

varmint_village = PettingZoo("Varmint Village")
slig = PettingZoo("Varmint Village")
varmint_village.animals.append(connie)
varmint_village.animals.append(bill)

for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

