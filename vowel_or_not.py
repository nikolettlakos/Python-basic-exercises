''' Write a function that takes a character (i.e. a string of length 1) 
and returns True if it is a vowel, False otherwise.
'''


def vowel_or_not(char):
    vowel = "aeiou"

    if char.lower() in vowel:
        return True
    else:
        return False


def main():
    print(vowel_or_not("A"))


if __name__ == '__main__':
    main()