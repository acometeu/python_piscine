import sys


def ft_isdigit(string: str, format: str):
    check = True
    for x in string:
        if (check is False):
            break
        check = False
        for y in format:
            if (x == y):
                check = True
                break
    return (check)


def whatis():
    args = sys.argv

    if (len(args) < 2):
        exit(1)
    elif (len(args) > 2):
        print("more than one argument is provided")
        exit(1)

    # remove operand
    if (len(args[1])):
        if (args[1][0] == '+' or args[1][0] == '-'):
            args[1] = args[1][1:]

    try:
        assert ft_isdigit(args[1], "1234567890"), "Arg is not an int"
        nbr = int(args[1])
    except AssertionError as error:
        print(error)
        exit(1)

    if (nbr % 2 == 0):
        print("I'm Even")
    else:
        print("I'm Odd")


def main():
    whatis()


if (__name__ == "__main__"):
    main()
