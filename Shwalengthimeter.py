test_strings = ["kawabunga", "metro2013", "moon", "orange"]


def shwalengthimeter(test_strings):
    list_of_strings = []
    for i in test_strings:
        new_word = "shwa"
        word_len = str(len(i))
        i = i[1:]
        if i[0] in ["a", "e", "o", "i", "u", "y"]:
            i = i[1:]
        new_word += i + " " + word_len
        list_of_strings.append(new_word)
    return list_of_strings


print(shwalengthimeter(test_strings))
