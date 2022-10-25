def pyramid(floor_size, size=2):
    pyramid_drawing = []
    spaces = 0
    while floor_size > 0:
        stars = " " * spaces + "*" * floor_size
        pyramid_drawing.insert(0, stars)
        floor_size -= size
        spaces += int(size/2)
    pyramid_drawing = "\n".join(pyramid_drawing)
    return pyramid_drawing

print(pyramid(11, 1))
print(pyramid(11, 2))
print(pyramid(11, 3))
print(pyramid(11, 4))

