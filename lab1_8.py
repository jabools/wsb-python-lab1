def counter(func):
    def wrapper(*args, **kwargs):
        func.counter += 1
        print('{0} was called {1} times'.format(func.__name__, func.counter))
        return func(*args, **kwargs)

    func.counter = 0
    return wrapper


@counter
def test_func():
    print('test function')


@counter
def test_func_2():
    print('second test function')


def main():
    for el in range(0, 3):
        test_func()

    for el in range(0, 7):
        test_func_2()


if __name__ == '__main__':
    main()
