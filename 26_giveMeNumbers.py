def test_me(x=333, y=7553):
    return ','.join([str(num) for num in range(x, y + 1) if num % 7 == 0 and num % 13 == 0 and num % 5 != 0])

def test_me2(x=333, y=7553):
    a = []
    while x <= y:
        if x % 7 == 0:
            if x % 13 == 0 and x % 5 != 0:
                a.append(str(x))
                x += 7
            else:
                x += 7
        else:
            x += 1 
    return ','.join(a)

print(test_me())
print(test_me2())
                      