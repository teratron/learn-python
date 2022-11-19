# Публичный
class A:
    text = "публичный"

    def public(self):
        print(f"Это {self.text} метод!")


a = A()
a.public()  # Это публичный метод!


# Защищённый
class B:
    _text = "защищённый"

    def _protected(self):
        print(f"Это {self._text} метод!")


b = B()
b._protected()  # Это защищённый метод!


# Приватный
class C:
    __text = "приватный"

    def __private(self):
        print(f"Это {self.__text} метод!")


c = C()

# c.__private()
# Traceback (most recent call last):
# AttributeError: 'C' object has no attribute '__private'. Did you mean: '_B__private'?

# Нарушение инкапсуляции
c._C__private()  # type: ignore # Это приватный метод!
