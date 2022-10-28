FRIENDS = [
    ["Python", "Drawing", "Games", "Girls", "Weapons", "Games", "Books"],
    ["Music", "Politics", "Books", "Girls", "Python", "Cinema", "Cars"],
    ["Cinema", "Music", "Drawing", "Python", "Books", "History"],
    ["War", "Sport", "Books", "Games", "Python", "Cinema", "Cars"],
    ["Knifes", "Games", "Books", "Girls", "Cinema", "Cars", "Python"],
    ["Sport", "Drawing", "Books", "Girls", "Games", "Music"],
]


def get_common_topics(friends=FRIENDS, topics=3):
    # removing duplicates from original list and converting it back to one
    friends = list(map(list, [set(friend) for friend in friends]))
    flatten_the_list = [j for i in friends for j in i]
    flatten_the_list.sort()  # dictionary keys will be alphabetically
    common_topics = {i: flatten_the_list.count(i) for i in flatten_the_list}
    most_popular = max(list(common_topics.values()))
    set_of_common_topics = set()
    while most_popular != 0:
        for key, values in common_topics.items():
            if values == most_popular:
                set_of_common_topics.add(key)
            if len(set_of_common_topics) == topics:
                # if the numbers in set is equal to needed topics, break out of for loop and set value to exit while loop
                most_popular = 1
                break
        most_popular -= 1
    return set_of_common_topics


print(get_common_topics())
