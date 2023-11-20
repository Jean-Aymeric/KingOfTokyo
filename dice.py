from abc import ABC

from abstractbehaviorroll import AbstractBehaviorRoll
from abstractside import AbstractSide
from lastroll import LastRoll
from realroll import RealRoll


class Dice(ABC):
    __sides: [AbstractSide]
    __lastSide: AbstractSide
    __behaviorRoll: AbstractBehaviorRoll

    def __init__(self):
        self.__sides = []
        self.__lastSide = None
        self.__behaviorRoll = RealRoll(self)

    def _addSide(self, side: AbstractSide) -> None:
        self.__sides.append(side)

    def roll(self) -> str:
        self.__lastSide = self.__behaviorRoll.roll()
        return self.__lastSide.getValue()

    @property
    def NumberOfSides(self) -> int:
        return len(self.__sides)

    @property
    def LastSide(self) -> AbstractSide:
        return self.__lastSide

    @property
    def Sides(self) -> [AbstractSide]:
        return self.__sides

    def keep(self) -> None:
        self.__behaviorRoll = LastRoll(self)

    @property
    def BehaviorRoll(self) -> AbstractBehaviorRoll:
        return self.__behaviorRoll

    @BehaviorRoll.setter
    def BehaviorRoll(self, behaviorRoll: AbstractBehaviorRoll) -> None:
        self.__behaviorRoll = behaviorRoll
