class A:
    def _protected(self):
        print("Это протектед метод!")


a = A()
a._protected()  # Это протектед метод!


class B:
    def __private(self):
        print("Это приватный метод!")


b = B()
# b.__private()
# Traceback (most recent call last):
# AttributeError: 'B' object has no attribute '__private'. Did you mean: '_B__private'?

b._B__private()  # type: ignore # Это приватный метод!
