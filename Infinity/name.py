from Infinity.exceptions import NameError


class Name:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return str(self)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) < 3:
            raise NameError(f"Name must have at least 2 symbols: {value}")
        if len(value) == None:
            raise NameError(f"Name cannot be empty")
        self.__value = value
