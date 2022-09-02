class Person:
    def __init__(self):
        self._name = None

    def get_name(self):
        print('get_name called')
        return self._name

    def set_name(self, i):
        print('set_name called')
        self._name = i

    def del_name(self):
        print('del_name called')
        del self._name

    name = property(get_name, set_name, del_name, "Person's Name Attribute")


if __name__ == '__main__':
    d = Person()
    d.name = 'Pankaj'
    print(d.name)
    del d.name
