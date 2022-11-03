from re import split

s = "Hello 123 Johnny B2 137"


def sep_strings(s):
    separated = [[], [], []]
    for i in split(" |\n", s):
        if i.isalpha():
            separated[0].append(i)
        elif i.isdigit():
            separated[1].append(int(i))
        elif i != "":
            separated[2].append(i)
    return separated


# oneline solution, above one is faster
def sep_strings2(s):
    return [
        [i for i in split(" |\n", s) if i.isalpha()],
        [int(i) for i in split(" |\n", s) if i.isdigit()],
        [
            i
            for i in split(" |\n", s)
            if not i.isalpha() and not i.isdigit() and i != ""
        ],
    ]


print(sep_strings(s))
print(sep_strings2(s))
