import numpy as np


def calcul_bmi(height: int | float, weight: int | float) -> int | float:
    '''Custom ufunc created with numpy for give_bmi that calcul bmi'''
    return (weight / (height * height))


def give_bmi(height: list[int | float], weight: list[int | float]
             ) -> list[int | float]:
    '''Calcul and return bmi'''
    try:
        assert isinstance((height), list
                          ), "Error: give_bmi must take list as args"
        assert isinstance((weight), list
                          ), "Error: give_bmi must take list as args"
    except Exception as error:
        print(error)
        return
    try:
        np_height = np.array(height, dtype='f')
        np_weight = np.array(weight, dtype='f')
    except Exception:
        print("Error: give_bmi take only list of int or float numbers")
        return

    calculbmi = np.frompyfunc(calcul_bmi, 2, 1)
    newlist = list(calculbmi(np_height, np_weight))
    return (newlist)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''Check if the bmi (1st arg) surpass a certain limit (2nd arg)'''
    try:
        assert isinstance(bmi, list
                          ), "Error: apply_limit must take list as args"
    except Exception as error:
        print(error)
        return
    try:
        np_bmi = np.array(bmi, dtype='f')
    except Exception:
        print("Error: apply_limit take only "
              "list of int or float numbers as first arg")
        return
    try:
        assert isinstance(limit, int
                          ), "Error: Apply_limit second arg must be an int"
    except Exception as error:
        print(error)
        return

    newlist = []
    for x in np_bmi:
        if x > limit:
            newlist.append(True)
        else:
            newlist.append(False)
    return newlist


def main():
    height = [2, 1]
    weight = [100, 30]
    notheight = [2, 'a']

    # give_bmi tests
    # list of float
    bmi = give_bmi(height, weight)
    print(f"give_bmi list of float : {bmi}")
    # list of int
    bmi = give_bmi([int(2), int(1)], weight)
    print(f"give_bmi list of int : {bmi}")
    # list of str
    bmi = give_bmi(notheight, weight)
    print(f"give_bmi list of str : {bmi}")
    # tupple of nbr
    bmi = give_bmi((2, 1), (100, 30))
    print(f"give_bmi tupple of nbr : {bmi}")
    # map set of nbr
    bmi = give_bmi({1: 1, 2: 2}, weight)
    print(f"give_bmi set of nbr : {bmi}")

    # apply_limit tests
    # list of floats
    print("apply_limit list of floats : "
          f"{apply_limit([25.5, 26, 27.7, 10, 100.0], 26)}")
    # list of int
    print("apply_limit list of floats : "
          f"{apply_limit([25, 26, 27, 10, 100], 26)}")
    # tupple of float
    print("apply_limit list of floats : "
          f"{apply_limit((25, 26, 27, 10, 100), 26)}")
    # second arg not int
    print("apply_limit list of floats : "
          f"{apply_limit([25, 26, 27, 10, 100], 'a')}")


if (__name__ == "__main__"):
    main()
