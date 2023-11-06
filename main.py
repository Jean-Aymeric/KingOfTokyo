from coin import Coin
from kingoftokyiodice import KingOfTokyoDice
from side import Side

dices = [KingOfTokyoDice(), Coin()]

for dice in dices:
    print(dice.roll())

for side in list(Side):
    print(side.getValue())
