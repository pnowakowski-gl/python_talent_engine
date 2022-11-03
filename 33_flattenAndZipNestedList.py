from itertools import zip_longest


def flat_zip(list1, list2):
    a = list(zip_longest(list1, list2))
    return [
        element
        for i in list(zip_longest(list1, list2))
        for element in i
        if element is not None
    ]


print(flat_zip([1, 2, 3], "ABCDEF"))
print(flat_zip([1, 2, 3], [2, 3, 4, 45]))
