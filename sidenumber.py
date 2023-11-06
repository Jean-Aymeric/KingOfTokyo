from abstractside import AbstractSide


class SideNumber(AbstractSide):
    def __init__(self, number: int):
        super().__init__(str(number))
