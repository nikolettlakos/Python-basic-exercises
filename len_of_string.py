''' Define a function that computes the length of a given list or string. '''


def length_of_something(given_thing):
    count = 0 

    for i in given_thing:
        count += 1
    return count


def main():
    list_given = [[2, 3, 5, 6], [2, 4, 6]]
    print(length_of_something(list_given))


if __name__ == '__main__':
    main()