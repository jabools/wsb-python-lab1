def method_decorator(func):
    def wrapper(*args, **kwargs):
        print('Function name: ' + func.__name__)
        print('Function args: ')
        print(args)
        print('Function named args: ')
        print(kwargs)
        return func(*args, **kwargs)

    return wrapper


@method_decorator
def print_text():
    print('Simple text')


@method_decorator
def print_given_text(text):
    print('Text: ' + text)


def main():
    print_text()
    print_given_text('test123')


if __name__ == '__main__':
    main()
