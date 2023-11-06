from abc import ABC

from abstractside import AbstractSide


class SideSymbol(AbstractSide, ABC):
    def __init__(self, symbol: str):
        super().__init__(symbol)
