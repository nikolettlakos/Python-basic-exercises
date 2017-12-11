''' Write a function is_member() that takes a value (i.e. a number, string, etc) 
x and a list of values a, 
and returns True if x is a member of a, False otherwise. '''


def is_member(x, a):
    if x in a:
        return True
    return False


def main():
    list_of_things = ["something", "cat", 1, 4.0]
    print(is_member("something", list_of_things))

if __name__ == '__main__':
    main()