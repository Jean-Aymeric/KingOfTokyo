import random

from abstractbehaviorroll import AbstractBehaviorRoll


class RealRoll(AbstractBehaviorRoll):
    def __init__(self, dice):
        super().__init__(dice)

    def roll(self):
        return self.Dice.Sides[random.randint(0, self.Dice.NumberOfSides - 1)]
