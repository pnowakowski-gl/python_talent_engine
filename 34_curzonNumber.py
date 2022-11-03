from math import pow


def is_curzon(num):
    return not bool(((pow(2, num) + 1) % (2 * num + 1)))
