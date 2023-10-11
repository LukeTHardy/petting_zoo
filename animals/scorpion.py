from datetime import date
from .animal import Animal
from movements import Slithering


class Scorpion(Animal, Slithering):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
