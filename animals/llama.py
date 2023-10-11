from .animal import Animal
from movements import Walking


class Llama(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift

    def feed_llama(self):
        print("TINA eat the FOOD")
