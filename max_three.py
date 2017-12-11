''' Define a function max_of_three() that takes three numbers as arguments and 
returns the largest of them.
'''


def max_of_three(num1, num2, num3):
    largest_number = int(num1)
    numbers = [num1, num2, num3]

    for x in numbers:
        if largest_number < x:
            largest_number = x
    return largest_number


def main():
    print(max_of_three(2, 5, 10))


if __name__ == '__main__':
    main()