list_ = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]


def rec_func(list_):
    sum_ = 0
    for i in list_:
        if type(i) == list:
            sum_ += rec_func(i)
        else:
            sum_ += i
    return sum_


def rec_func2(list_):
    a = "".join([str(i) for i in list_])
    return sum([int(i) for i in a if i.isdigit()])


# print(rec_func(list_))
print(rec_func2(list_))
