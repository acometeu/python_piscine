'''
This program count the number of all characters in a single string argument
and it count the numbers of 5 specials type characters :
-upper letters
-lower letters
-punctuation marks
-spaces
-digits
'''

import sys


def count_characters(text: str):
    '''takes the string to count character from'''
    upper_letters = 0
    lower_letters = 0
    punctuations = 0
    spaces = 0
    digits = 0
    punctuations_list = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    for char in text:
        if (char.isdigit()):
            digits += 1
        elif (char.isspace()):
            spaces += 1
        elif (char in punctuations_list):
            punctuations += 1
        elif (char.isupper()):
            upper_letters += 1
        elif (char.islower):
            lower_letters += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper_letters} upper letters")
    print(f"{lower_letters} lower letters")
    print(f"{punctuations} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    '''program must take a string
    can't take more than 2 args'''
    try:
        assert len(sys.argv) <= 2, \
            "Invalid arg: this program cannot take more than 1 argument"
    except AssertionError as error:
        print(error)
        exit(1)

    if (len(sys.argv) == 2):
        text = sys.argv[1]
    else:
        print("Prompt a string...")
        text = sys.stdin.readline()
    if (text == ""):
        print("Program needs a string to count characters from")
        exit(1)

    count_characters(text)


if (__name__ == "__main__"):
    main()
