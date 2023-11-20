from enum import Enum

from abstractside import AbstractSide
from fist import Fist
from heart import Heart
from sidenumber import SideNumber
from thunder import Thunder


class Side(Enum):
    __side: AbstractSide

    FIST = Fist(),
    HEART = Heart(),
    THUNDER = Thunder(),
    ONE = SideNumber(1),
    TWO = SideNumber(2),
    THREE = SideNumber(3)

    def __init__(self, side: AbstractSide):
        self.__side = side

    def getValue(self) -> str:
        return self.__side.getValue()
