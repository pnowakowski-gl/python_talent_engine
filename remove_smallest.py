def remove_smallest(num, list_):
    new_list = list_.copy()
    to_del = list_.copy()
    to_del.sort()
    for i in to_del[:num]:
        new_list.remove(i)
    return new_list


print(remove_smallest(3, [1, 2, 3, 1, 2, 4]))
print(remove_smallest(2, [5, 4, 1, 3]))
print(remove_smallest(4, [1, 2, 1]))
