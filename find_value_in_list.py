''' Write a function is_member() that takes a value (i.e. a number, string, etc) 
x and a list of values a, 
and returns True if x is a member of a, False otherwise. 
(Note that this is exactly what the in operator does, but for the sake of the exercise 
you should pretend Python did not have this operator.)'''


def is_member(x, a):
    for thing in a:
        if thing == x:
            return True
        return False


def main():
    list_of_things = ["something", "cat", 1, 4.0]
    print(is_member("something", list_of_things))

if __name__ == '__main__':
    main()


'''
    if x in a:
        return True
    return False

Solution with the in operator '''