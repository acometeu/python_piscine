def NULL_not_found(object: any) -> int:
    if (object is None):
        print(f"Nothing: None {type(object)}")
    elif (type(object) is float):
        print(f"Cheese: nan {type(object)}")
    elif (type(object) is int and object == 0):
        print(f"Zero: 0 {type(object)}")
    elif (type(object) is str and object == ""):
        print(f"Empty: {type(object)}")
    elif (type(object) is bool and object is False):
        print(f"Fake: False {type(object)}")
    else:
        print("Type not Found")
        return (1)
    return (0)
