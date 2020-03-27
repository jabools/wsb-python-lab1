def is_prime(number: int):
    if number <= 1 or not number % 2:
        return False

    for el in range(2, number):
        if not number % el:
            return False

    return True


def get_primes_filter(collection: list):
    return list(filter(lambda arg: is_prime(arg), map(lambda arg: int(arg), collection)))


def get_primes_comprehension(collection: list):
    return [int(el) for el in collection if is_prime(el)]


def main():
    my_list = list(range(0, 100))
    print('Initial list:')
    print(my_list)

    print('\nFilter and map results:')
    print(get_primes_filter(my_list))

    print('\nList comprehension results:')
    print(get_primes_comprehension(my_list))


if __name__ == '__main__':
    main()
