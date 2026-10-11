from enum import Enum


class FarmAnimal(Enum):
    SHEEP = ((0,0), (0,1), (0,2), (0,3))
    PIG = ((0,0), (1,0), (0,1), (1,1))
    RABBIT = ((0,0), (1,0), (2,0), (3,0))
    HORSE = ((0,0), (1,0), (2,0))
    COW = ((0,0), (0,1), (0,2))
    UNICORN = ((0,0), (1,1), (1,2))

    def __str__(self):
        return self.name.capitalize()

class OutbackAnimal(Enum):
    KANGAROO = ((0,0), (1,1), (2,2), (3,3))
    PLATYPUS = ((0,0), (0,1), (1,1), (1,2))
    CROCODILE = ((0,0), (0,1), (0,2), (0,3))
    KOALA = ((0,0), (0,1), (1,1))
    COCKATOO = ((0,0), (1,1), (2,1))
    TIDALICK = ((1,0), (0,1), (1,2))

    def __str__(self):
        return self.name.capitalize()

class SavannahAnimal(Enum):
    GIRAFFE = ((0,0), (1,0), (2,0), (3,0))
    ZEBRA = ((1,0), (0,1), (1,2), (2,1))
    HIPPO = ((0,0), (0,2), (2,0), (2,2))
    ELEPHANT = ((0,0), (1,0), (0,1))
    LION = ((0,0), (0,1), (0,2))
    GRYPHON = ((0,0), (1,1), (0,2))

    def __str__(self):
        return self.name.capitalize()

class NorthernAnimal(Enum):
    BEAVER = ((1,0), (1,1), (0,2), (2,2))
    BEAR = ((0,0), (0,1), (1,1), (2,1))
    SKUNK = ((1,0), (1,1), (0,1), (0,2))
    MOOSE = ((0,0), (1,1), (0,2))
    FOX = ((0,0), (0,1), (1,2))
    SASQUATCH = ((0,0), (1,0))

    def __str__(self):
        return self.name.capitalize()

class PolarAnimal(Enum):
    SEAL = ((0,0), (1,1), (2,2), (1,3))
    MUSKOX = ((0,0), (1,0), (0,1), (1,2))
    PENGUIN = ((0,1), (1,1), (2,2), (2,0))
    POLAR_BEAR = ((0,0), (0,2), (1,2))
    WALRUS = ((0,0), (1,1), (1,2))
    YETI = ((0,0), (2,0))

    def __str__(self):
        return self.name.replace("_"," ").title()

REGIONS = {
    "FARM": FarmAnimal,
    "OUTBACK": OutbackAnimal,
    "SAVANNAH": SavannahAnimal,
    "NORTHERN": NorthernAnimal,
    "POLAR": PolarAnimal
}


