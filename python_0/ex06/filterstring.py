import sys


def filterstring(S: str, N: int) -> list:
    '''Return a list containing all the words in S separated
    by space and containing more than N characteres'''
    larger_than_N = []
    larger_than_N.append(lambda x: len(x) > N)
    newlist = [x for x in S.split(" ") if larger_than_N[0](x)]
    print(newlist)


def main():
    '''Program must take 2 args : a strings of alphanumerical
    characteres and an int'''
    args = sys.argv
    try:
        assert len(args) == 3, "Program must take 2 arguments"
        assert all(x.isalnum() or x.isspace() for x in args[1]), (
            "Program 1st arg must be alpha numerical")
        assert args[2].isdigit(), "Program 2nd arg must be an int"
    except AssertionError as error:
        print(error)
        return (1)

    filterstring(args[1], int(args[2]))


if (__name__ == "__main__"):
    main()
