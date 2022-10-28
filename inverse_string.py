string_ = "Revert me please:)"


def method_1(string_):
    return string_[::-1]


def method_2(string_):
    string_ = list(string_)
    string_.reverse()
    string_ = "".join(string_)
    return string_


def method_3(string_):
    a = []
    """
    for i in string_[::-1]: would work too but it's too similar to first method
    """
    for i in range(len(string_) - 1, -1, -1):
        a.append(string_[i])
    string_ = "".join(a)
    return string_


print("1 -->", method_1(string_))
print("2 -->", method_2(string_))
print("3 -->", method_3(string_))
