from .attraction import Attraction
from movements import Swimming


class Wetlands(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal_pythonic(self, animal):
        try:
            if animal.swim_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as err:
            print(
                f'{animal} doesn\'t swim, so please do not put it in the {self.attraction_name} attraction.')
