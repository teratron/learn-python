import datetime


class User:
    def __init__(self, first_name='', last_name='', email='', password=()):
        self._id: int
        self._first_name: str = first_name
        self._last_name: str = last_name
        self._date_birth: datetime = datetime.datetime(1969, 9, 30, 13, 0, 0, 0)
        self._email: str = email
        self.__password: tuple = password

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name
