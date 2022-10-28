test_data = ["az", "toto", "picaro", "zone", "kiwi"]
test_data2 = [
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
]


def partlist(list_):
    return [
        (" ".join(list_[0:i]), " ".join(list_[i : len(list_)]))
        for i in range(1, len(list_))
    ]


print(partlist(test_data))
print(partlist(test_data2))
