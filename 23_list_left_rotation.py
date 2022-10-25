list_ = list("1234567")

def left_rotate(l, num):
    list_a = l[:num]
    list_b = l[num:]
    return list_b + list_a

# Tests:
print(left_rotate(list_, 4)) # should be ["5", "6", "7", "1", "2", "3", "4"]
print(left_rotate(list_, 5) is not list_) # should be True