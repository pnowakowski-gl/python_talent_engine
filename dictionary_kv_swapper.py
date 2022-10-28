data = {
    "key1": 25,
    100: "value100",
    "cadabra": "abra",
    (1, 2): (3, 4),
    "shmobject": object,
    False: None,
}
print(data[0])


def dict_swap(data):
    swapped_data = dict()
    for key, value in data.items():
        try:
            swapped_data[value] = key
        except TypeError:
            continue

    return swapped_data


print(dict_swap(data))

# Advanced task (#2 in tests):
tricky_data = {"cadabra": "abra", (1, 2): [3, 4], "oops": {}}
print(dict_swap(tricky_data))
