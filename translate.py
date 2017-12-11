''' Write a function translate() that will translate a text into "rövarspråket" 
(Swedish for "robber's language"). That is, double every consonant and place an 
occurrence of "o" in between. For example, translate("this is fun") should return the string 
"tothohisos isos fofunon".
'''


def translate(word):
    consonant = "bcdfghjklmnpqrstvwxyz"

    translate = []
    for char in word:
        if char in consonant:
            character_append = char + "o" + char
            translate.append(character_append)
        else:
            translate.append(char)
    
    translate = "".join(translate)
    return translate


def main():
    print(translate("rövarspråket"))


if __name__ == '__main__':
    main()