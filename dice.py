import random
from abc import ABC

from abstractside import AbstractSide


class Dice(ABC):
    __sides: [AbstractSide]

    def __init__(self):
        self.__sides = []

    def _addSide(self, side: AbstractSide) -> None:
        self.__sides.append(side)

    def roll(self) -> str:
        return random.choice(self.__sides).getValue()
