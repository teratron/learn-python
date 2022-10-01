class User:
    def __init__(self, name):
        self._id: int = 0
        self._name: str = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
