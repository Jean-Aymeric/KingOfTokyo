from dice import Dice
from side import Side


class KingOfTokyoDice(Dice):
    def __init__(self):
        super().__init__()
        self._addSide(Side.FIST)
        self._addSide(Side.HEART)
        self._addSide(Side.THUNDER)
        self._addSide(Side.ONE)
        self._addSide(Side.TWO)
        self._addSide(Side.THREE)
