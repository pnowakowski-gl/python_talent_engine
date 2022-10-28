def filter_numbers(start=1000, end=5000):
    return list(filter(lambda x: x % 3 == 0, range(start, end)))


def filter_numbers(start=1000, end=5000):
    return list(
        filter(
            lambda x: x
            if all([True if int(i) in [0, 3, 6, 9] else False for i in str(x)])
            else "",
            range(start, end),
        )
    )


print(filter_numbers(3000, 3010))
