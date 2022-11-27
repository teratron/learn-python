print('main.py')

# 1
# import package.file1
# import package.file2
#
# print(package.file1.b)
# print(package.file2.d)

# 2
# from package import file1
# from package import file2
# from package.file2 import h
#
# print(file1.b)
# print(file2.d)
# print(h)

# 3
# add __init__.py to package directory
# import package
#
# print(package.h)

# 4
# import package
#
# print(package.file1.aaa())
# print(package.file2.d)

# 5
import package

print(package.a)
print(package.file2.d)

# if __name__ == '__main__':
#     print(__name__)
