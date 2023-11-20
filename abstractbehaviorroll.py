from abc import ABC, abstractmethod


class AbstractBehaviorRoll(ABC):
    def __init__(self, dice):
        self.__dice = dice

    @property
    def Dice(self):
        return self.__dice

    @Dice.setter
    def Dice(self, dice):
        self.__dice = dice

    @abstractmethod
    def roll(self):
        pass
