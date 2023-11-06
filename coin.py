from dice import Dice
from side import Side


class Coin(Dice):
    def __init__(self):
        super().__init__()
        self._addSide(Side.HEAD)
        self._addSide(Side.TAILS)
