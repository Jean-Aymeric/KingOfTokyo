from abstractbehaviorroll import AbstractBehaviorRoll
from realroll import RealRoll


class LastRoll(AbstractBehaviorRoll):
    def __init__(self, dice):
        super().__init__(dice)

    def roll(self):
        self.Dice.BehaviorRoll = RealRoll(self.Dice)
        return self.Dice.LastSide
