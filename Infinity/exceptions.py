class PhoneMustBeNumber(Exception):
    pass


class BirthdayException(Exception):
    pass


class EmailException(Exception):
    pass


class Name_Error(Exception):
    def __str__(self) -> str:
        return super().__str__()
