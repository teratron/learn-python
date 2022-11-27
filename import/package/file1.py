print('file1.py')

import file2

print(file2.d)

# 5
# работает только со звёздочкой (*)
__all__ = ['a', 'aaa']

a = 11
b = 20
c = 24.5


def aaa():
    print('function aaa')
