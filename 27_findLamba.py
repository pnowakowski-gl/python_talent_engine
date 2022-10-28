def find_lambda(list_):
    func = 0
    for i in range(len(list_)):
        print
        if isinstance(list_[i], type(lambda: 0)):
            # these 2 works too, they check if object is callable so is it a function
            # if '__call__' in dir(list_[i]):
            # if callable(list_[i]):
            func = i
            break
    list_without_lambda = list_.copy()
    list_without_lambda.remove(list_[func])
    return list(map(list_[func], list_without_lambda))


print(find_lambda([lambda a: a + 2, 9, 3, 1, 0]))  # [11, 5, 3, 2]
print(find_lambda([9, 2, 3, lambda a: a / 2.0, 1, 0]))  # [4.5, 1, 1.5, 0.5, 0.0]
