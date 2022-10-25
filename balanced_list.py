def gen_list(num=3):
    return [*range(1, num), sum(range(1, num))*-1]

print(gen_list())
print(gen_list(5))
print(gen_list(10))