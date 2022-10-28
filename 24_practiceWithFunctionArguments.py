def gen_mul_table(
    width=10, height=10, *, sep_width=3, print_header=False, print_footer=True
):
    header = f"Multiplication Table {width} x {height}\n" if print_header else ""
    footer = "\n" + "-" * 30 if print_footer else ""
    mul_table = "".join(
        [
            " " * (sep_width - len(str(j))) + str(j) + "\n"
            if ind % width == width - 1
            else " " * (sep_width - len(str(j))) + str(j)
            for ind, j in enumerate(
                [i * j for i in range(1, height + 1) for j in range(1, width + 1)]
            )
        ]
    )[:-1]
    return f"{header + mul_table + footer}"


print(gen_mul_table(3, 3, sep_width=3, print_header=True, print_footer=True))
print(gen_mul_table(3, 11, sep_width=6, print_header=False, print_footer=True))
print(gen_mul_table(12, 12, sep_width=4, print_header=False, print_footer=False))
print(gen_mul_table(3, 3, print_footer=False))

"""
Second solution with f-formatting:
result = ''
for ind, i in enumerate([i*j for i in range(1, 11) for j in range(1, 11)]):
    result += f"{i:4}"
    if ind % 10 == 9:
        result += '\n'
print(result)

"""
