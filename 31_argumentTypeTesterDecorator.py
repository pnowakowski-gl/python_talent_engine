def check_arg_types(strings_allowed=True, numbers_allowed=True, sequences_allowed=True):
    """Parametrized decorator"""

    def deco(func):
        def arguments(*args):
            for i in [*args]:
                if (
                    (not strings_allowed and type(i) == str)
                    or (not numbers_allowed and type(i) in (int, float))
                    or (not sequences_allowed and type(i) in (list, tuple, dict))
                ):
                    raise TypeError

        return arguments

    return deco


@check_arg_types(strings_allowed=False, numbers_allowed=False, sequences_allowed=False)
def func(*args):
    print("Working ok")


try:
    func("hello", "test", (1, 2))  # working OK
except TypeError:
    print("TypeError1")

try:
    func("string", 1)  # raise TypeError
except TypeError:
    print("TypeError2")

try:
    func({1: 1, 2: 2})
except TypeError:
    print("TypeError3")

try:
    func({1, 2, 3})  # working OK
except TypeError:
    print("TypeError4")

try:
    func(1.23, (1, 2), "what")  # working OK
except TypeError:
    print("TypeError5")
