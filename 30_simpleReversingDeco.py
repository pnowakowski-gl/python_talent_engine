def deco(f):
    def reverse():
        return str(f())[::-1]

    return reverse


@deco
def test_me():
    return True


print(test_me())  # "eurT"
