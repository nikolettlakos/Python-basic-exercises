''' Define a function max() that takes two numbers as arguments and returns the largest of them. 
Use the if-then-else construction.'''


def max(num_1, num_2):
    largest_number = ""
    if num_1 > num_2:
        largest_number = num_1
    elif num_1 < num_2:
        largest_number = num_2
    else: 
        largest_number = num_1

    return int(largest_number)


def main():
    print(max(6.0, 6))


if __name__ == '__main__':
    main()


'''
def max(num_1, num_2):
    if num_1 > num_2:
        return num_1
    return num_2

or

return num1 if num1 > num 2 else num 2
'''
