def repeater(num_of_repeats=1):
    def outer_decorator(func):
        def inner_decorator(*args, **kwargs):
            if num_of_repeats > 0:
                for _ in range(num_of_repeats):
                    print(func(*args, **kwargs))
            else:
                print(func(*args, **kwargs))

        return inner_decorator

    return outer_decorator


@repeater(3)
def print_text(message):
    return f'Вам сообщение: {message}'


if __name__ == "__main__":
    print_text('Просыпайся!')
