from .animal import Animal
from movements import Walking, Swimming


class Turtle(Animal, Walking, Swimming):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        Swimming.__init__(self)
        self.shift = shift
