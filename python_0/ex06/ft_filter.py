import test_function


def ft_filter(function, iterable):
    '''
    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true.
    '''
    try:
        iter(iterable)
    except TypeError:
        print("Error: ft_filter second arg must be iterable")
        return (iter([]))

    if (callable(function)):
        try:
            newlist = [x for x in iterable if function(x)]
        except Exception:
            print("Error: Either function not acceptable or function "
                  "and iterator not compatible")
            newlist = []
    elif (function is None):
        newlist = [x for x in iterable if x != 0 and x != ""]

    return (iter(newlist))


def main():
    nbrs = [-1, 0, 1, 2, 3]
    strs = ["hello", "ouioui", "", "hihihaha"]

    # ERRORS CASES
    # second arg not iterable
    new_list = ft_filter(test_function.ft_is_odd, 42)
    for x in new_list:
        print(f"ft_filter without an iterator : {x}")

    # first arg isn't a valid function
    new_list = ft_filter(test_function.ft_hello_world, strs)
    for x in new_list:
        print(f"ft_filter with wrong func : {x}")

    # WORKING CASES
    # with ints
    new_list = ft_filter(test_function.ft_is_odd, nbrs)
    for x in new_list:
        print(f"ft_filter with \"ft_is_odd\" and list of int : {x}")

    new_list = filter(test_function.ft_is_odd, nbrs)
    for x in new_list:
        print(f"filter with \"ft_is_odd\" and list of int : {x}")

    # with strings
    new_list = ft_filter(test_function.ft_len_is_more_than_5, strs)
    for x in new_list:
        print("ft_filter with \"ft_is_len_longer_than_5\" and "
              f"list of str : {x}")

    new_list = filter(test_function.ft_len_is_more_than_5, strs)
    for x in new_list:
        print(f"filter with \"ft_is_len_longer_than_5\" and list of str : {x}")

    # with function none and ints
    new_list = ft_filter(None, nbrs)
    for x in new_list:
        print(f"ft_filter with func \"none\" : {x}")

    new_list = filter(None, nbrs)
    for x in new_list:
        print(f"filter with func \"none\" : {x}")


if (__name__ == "__main__"):
    main()
