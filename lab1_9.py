def count_words(file):
    count = 0
    
    with open(file, 'r', encoding='UTF-8') as fd:
        for line in fd:
            count += len(line.strip().split(' '))

    return count


def main():
    filename = 'lorem.txt'

    print('{0} file counts {1} words'.format(filename, count_words(filename)))


if __name__ == '__main__':
    main()
