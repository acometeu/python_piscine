import sys


def create_morse_dictionary():
    '''Create a morse dictionary'''
    morse_dictionary = {}
    morse_dictionary[' '] = "/"
    morse_dictionary['a'] = ".-"
    morse_dictionary['b'] = "-..."
    morse_dictionary['c'] = "-.-."
    morse_dictionary['d'] = "-.."
    morse_dictionary['e'] = "."
    morse_dictionary['f'] = "..-."
    morse_dictionary['g'] = "--."
    morse_dictionary['h'] = "...."
    morse_dictionary['i'] = ".."
    morse_dictionary['j'] = ".---"
    morse_dictionary['k'] = "-.-"
    morse_dictionary['l'] = ".-.."
    morse_dictionary['m'] = "--"
    morse_dictionary['n'] = "-."
    morse_dictionary['o'] = "---"
    morse_dictionary['p'] = ".--."
    morse_dictionary['q'] = "--.-"
    morse_dictionary['r'] = ".-."
    morse_dictionary['s'] = "..."
    morse_dictionary['t'] = "-"
    morse_dictionary['u'] = "..-"
    morse_dictionary['v'] = "...-"
    morse_dictionary['w'] = ".--"
    morse_dictionary['x'] = "-..-"
    morse_dictionary['y'] = "-.--"
    morse_dictionary['z'] = "--.."
    morse_dictionary['1'] = ".----"
    morse_dictionary['2'] = "..---"
    morse_dictionary['3'] = "...--"
    morse_dictionary['4'] = "....-"
    morse_dictionary['5'] = "....."
    morse_dictionary['6'] = "-...."
    morse_dictionary['7'] = "--..."
    morse_dictionary['8'] = "---.."
    morse_dictionary['9'] = "----."
    morse_dictionary['0'] = "-----"
    return (morse_dictionary)


def ft_translate_to_morse(string: str):
    ''' Function translate latin alphabet, arabic number and space in morse
        code
        Take 1 arg that is a string with only alphanumerical and space
        characters'''
    try:
        assert isinstance(string, str) is True, (
            "ft_translate_to_morse only take str")
        assert all(x.isalnum() or x.isspace() for x in string), (
            "ft_translate_to_morse only take alphanumerical "
            "and space character")
    except AssertionError as error:
        print(error)
        return (1)

    morse_dict = create_morse_dictionary()
    string = string.lower()
    i = 0
    while i < len(string) - 1:
        print(morse_dict[string[i]], end=' ')
        i += 1
    if (len(string)):
        print(morse_dict[string[i]])
    else:
        print('')


def main():
    '''Program only take one arg'''
    try:
        assert len(sys.argv) == 2, "ft_translate_to_morse only take 1 argument"
    except AssertionError as error:
        print(error)
        return (1)

    ft_translate_to_morse(sys.argv[1])


if (__name__ == "__main__"):
    main()
