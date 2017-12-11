''' Define a function overlapping() that takes two lists and returns True if they have at least one member in common, 
False otherwise. You may use your is_member() function, 
or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops. '''


def overlapping(list_a, list_b):
    for i in list_a:
        for j in list_b:
            if i == j:
                return True
    return False


def main():
    a = ["something", "cat", 1, 2, 5.4]
    b = ["2"]
    print(overlapping(a, b))

if __name__ == '__main__':
    main()