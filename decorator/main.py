def my_decorator(func):
    def wrapper():
        print('код, который выполняется до функции')
        func()
        print('код, который выполняется после работы функции')

    return wrapper


@my_decorator
def some_function():
    print('работает функция, которую мы задекорировали')


some_function()
