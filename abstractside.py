from abc import ABC


class AbstractSide(ABC):
    __value: str

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value
