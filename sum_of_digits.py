def sum_digits(input_str: str) -> int:
    a = 0
    for i in input_str:
        if i.isdigit():
            a += int(i)
    return sum([int(i) for i in input_str if i.isdigit()])
    
    
# Small tests
print(sum_digits("abc123___##05__5")) # 16
print(sum_digits("00000000000")) # 0
print(sum_digits("@@@@@@-1.0####")) # 1
print(sum_digits("100____½")) # 1