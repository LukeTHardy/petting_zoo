"""class imports"""
from datetime import date
from animals import Snake, Centipede, Scorpion, Worm, Salamander, Whale, Goose, Shark, Shrimp, Seahorse, Cthulhu, Bear, Giraffe, Lemur, Llama, Turtle
from attractions import SnakePit, Wetlands, PettingZoo, Attraction

class_action_park = PettingZoo(
    "Class Action Park", "smelly critters that will probably tolerate you touching them")
sssnake_pit = SnakePit(
    "Sssnake Pit", "horrifying critters that people actually keep as pets")
wet_dreams = Wetlands(
    "Wet Dreams", "moist critters that probably shouldn't be in tennessee")

miss_fuzz = Llama("Miss Fuzz", "domestic llama",
                  "midday", "cocoa puffs", 232425)
freddie = Giraffe("Freddie", "dwarf giraffe", "morning", "miracle gro", 454647)
pooh = Bear("Pooh", "pretend bear", "midday", "pretend local honey", 565758)
zub = Lemur("Zuhboomuhfoo", "tv host monkey",
            "afternoon", "smaller monkeys", 676869)
tuhtle = Turtle("Tuhtle", "viral turtle star", "morning", "upvotes", 787970)
class_action_park.add_animal(miss_fuzz)
class_action_park.add_animal(freddie)
class_action_park.add_animal(pooh)
class_action_park.add_animal(zub)
class_action_park.add_animal(tuhtle)

purgle = Whale("Purgle", "lightspeed space whale", "stardust", 358392)
bruce = Shark("Bruce", "vegan shark", "black bean burgers", 983124)
seabiscuit = Seahorse("Seabiscuit", "racing seahorse",
                      "plankton from spongebob", 546782)
albert = Shrimp("Albert", "delicious crustacean", "sea monkeys", 170238)
dave = Cthulhu("Dave", "reluctant sea monster",
               "souls of lost sailors", 123456789)
wet_dreams.add_animal(purgle)
wet_dreams.add_animal(bruce)
wet_dreams.add_animal(seabiscuit)
wet_dreams.add_animal(albert)
wet_dreams.add_animal(dave)

nagini = Snake("Nagini", "slytherin python", "wormtail", 384736)
arthur = Centipede("Arthur", "insect horror show", "crumbs of evil", 993843)
spud = Worm("Spud", "alaskan bull worm", "100 yukon gold potatoes", 112345)
dwayne = Scorpion("Dwayne", "cgi scorpion", "more pixels", 554738)
sally = Salamander("Sally", "cute wet lizard thing", "jello cup", 812398)
sssnake_pit.add_animal(nagini)
sssnake_pit.add_animal(arthur)
sssnake_pit.add_animal(spud)
sssnake_pit.add_animal(dwayne)
sssnake_pit.add_animal(sally)

walker_strings = ('\n').join(
    f'*{animal.name} the {animal.species}' for animal in class_action_park.animals)

crawler_strings = ('\n').join(
    f'*{animal.name} the {animal.species}' for animal in sssnake_pit.animals)

swimmer_strings = ('\n').join(
    f'*{animal.name} the {animal.species}' for animal in wet_dreams.animals)

gary = Goose("Gary", "silly goose", "white bread", 325476)
gary.run()
stink_town = Attraction("Stink Town", "critters that seriously need a bath")
stink_town.add_animal(gary)
for animal in stink_town.animals:
    print(animal)

# print(f"""{class_action_park.attraction_name} is where you'll find {class_action_park.description}, like:
# {walker_strings}""")
# print(f"""{wet_dreams.attraction_name} is where you'll find {wet_dreams.description}, like:
# {swimmer_strings}""")
# print(f"""{sssnake_pit.attraction_name} is where you'll find {sssnake_pit.description}, like:
# {crawler_strings}""")

# print(sssnake_pit.last_critter_added)

nagini.feed()

billy = Shark("Billy", "vegan shark", "faux sushi", 675890)
mollie = Llama("Mollie", "llama", "afternoon", "chips", 148239)

class_action_park.add_animal_pythonic(mollie)
class_action_park.add_animal_type_check(mollie)
class_action_park.add_animal_pythonic(billy)
