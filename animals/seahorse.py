from .animal import Animal
from movements import Swimming


class Seahorse(Animal, Swimming):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
