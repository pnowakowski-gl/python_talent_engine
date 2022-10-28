def flag(width=10, height=4):
    WHITE = "\u2B1c"
    RED = "\U0001F7E5"

    result = ""
    current_color = WHITE
    for i in range(height):
        if i >= height // 2:
            current_color = RED
        for _ in range(width):
            result += current_color
        result += "\n"
    return result


print(flag())
print(flag(11, 5))
print(flag(3))
