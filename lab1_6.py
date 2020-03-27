def fibonacci(n: int):
    if n < 0:
        raise Exception('Given number must be greater than 0')

    if not n:
        return 0

    if n < 3:
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1)


def main():
    number = int(input('Please enter a number: '))
    print('Fibonacci({0}) = {1}'.format(number, fibonacci(number)))


if __name__ == '__main__':
    main()
