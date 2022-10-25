def draw_table():
    enter_ = '\n'
    return ''.join([' ' * (4-len(str(j))) + str(j) + '\n' if ind % 10 == 9 else ' ' * (4-len(str(j))) + str(j) for ind, j in enumerate([i*j for i in range(1, 11) for j in range(1, 11)])])
    
print(draw_table())

'''
Second solution with f-formatting:
result = ''
for ind, i in enumerate([i*j for i in range(1, 11) for j in range(1, 11)]):
    result += f"{i:4}"
    if ind % 10 == 9:
        result += '\n'
print(result)

'''