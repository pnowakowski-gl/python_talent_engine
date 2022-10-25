from collections import Counter
from random import shuffle
test_list = ["tsar", "rat", "tar", "star", "tars", "cheese"]
test_list2 = ["cat", "bat", "tab", "tac", "tree", "erte", "coconut", "nutcoco"]
shuffle(test_list)
def group_anagrams(test_list):
    grouped_anagrams = []
    while test_list != []:
        new_group = []
        new_group.append(test_list.pop(0))
        i = 0
        while i < (len(test_list)):
            if Counter(test_list[i]) == Counter(new_group[0]):
                new_group.append(test_list.pop(i))
                i -= 1
            i += 1
        grouped_anagrams.append(new_group)
    return grouped_anagrams
print(group_anagrams(test_list))
print(group_anagrams(test_list2))
                                