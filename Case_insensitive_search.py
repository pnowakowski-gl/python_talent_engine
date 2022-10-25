def check(target: str, list_):
    list_ = [i.lower() for i in list_]
    if target.lower() in list_:
        return True
    else:
        return False

    # return target.lower() in [i.lower() for i in list_]
    
    
print(check("a", ["A", "b", "c"]))  # True
print(check("abc", ["AbC", "b", "c"]))  # True
print(check("aBc", ["AbC"]))  # True
print(check("abc", ["a", "b", "c"]))  # False
print(check("abc", []))  # False