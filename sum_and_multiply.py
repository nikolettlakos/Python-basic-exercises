''' Define a function sum() and a function multiply() that sums and multiplies (respectively)
 all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, 
 and multiply([1, 2, 3, 4]) should return 24.
'''


def sum(numbers):
    count = 0

    for x in numbers:
        count += x
    return count


def multiply(numbers):
    count = 1
    
    for x in numbers:
        count = count * x
    return count


def main():
    list_of_numbers = [1, 2, 3, 4]
    print(sum(list_of_numbers))
    print(multiply(list_of_numbers))

if __name__ == '__main__':
    main()