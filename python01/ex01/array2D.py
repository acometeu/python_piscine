import numpy as np


def slice_me_check_errors(family: list, start: int, end: int) -> bool:
    '''check some errors cases of the slice_me func'''
    try:
        assert isinstance(family, list), ("Error: slice_me must take"
                                          " a list as first arg")
        assert isinstance(start, int), ("Error: slice_me must take an int "
                                        "as second arg")
        assert isinstance(end, int), ("Error: slice_me must take an int "
                                      "as third arg")
    except AssertionError as error:
        print(error)
        return (1)


def slice_me(family: list, start: int, end: int) -> list:
    '''take a list and slice it at start (second arg)
       until before end (third arg)'''
    if (slice_me_check_errors(family, start, end)):
        return
    try:
        newlist = np.array(family)
        assert newlist.ndim == 2, "Error: 1st arg table dimension must be 2"
    except AssertionError as error:
        print(error)
        return
    except Exception:
        print("Error: 1st arg not a valid list")
        return

    print(f"My shape is : {newlist.shape}")
    newlist = newlist[start:end]
    print(f"My new shape is : {newlist.shape}")
    return newlist


def main():
    family = [[1, 2], [3, 4], [5, 6], [7, 8]]
    family2 = [[1, 2], [3, 4], [5, "ouioui"], [7, 8]]
    familybadshape1 = [[[1, 2], [3, 4], [5, "ouioui"], [7, 8]]]
    familybadshape2 = [1, 2, 3, 4, 5, 6, 7, 8]
    # classic case
    print(slice_me(family, -3, 10))

    # Error 1st arg not a list
    print(f"1 : {slice_me(4, 2, 3)}")
    # Error 2nd arg not an int
    print(f"2 : {slice_me(family, 2.0, 3)}")
    # Error 3rd arg not an int
    print(f"3 : {slice_me(family, 2, 'str')}")
    # Error 1st arg with to many dimensions
    print(f"4 : {slice_me(familybadshape1, 2, 3)}")
    # Error 1st arg without enough dimensions
    print(f"5 : {slice_me(familybadshape2, 2, 3)}")

    # list with string
    print(slice_me(family2, 2, 3))


if (__name__ == "__main__"):
    main()
