''' Define a function reverse() that computes the reversal of a string. For example, 
reverse("I am testing") 
should return the string "gnitset ma I". '''


def reverse(word):
    word = word[:: -1]
    return word


def printing(test):
    print(test)


def main():
    reverse("I am testing")
    printing(reverse("I am testing"))


if __name__ == '__main__':
    main()