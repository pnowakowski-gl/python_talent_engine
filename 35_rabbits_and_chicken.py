def count_rabbits_chickens(heads, legs, rabbits=0, chickens=0):
    # if the number of legs is odd, is lower than two times heads
    # or higher than 4 times legs, then it's already not possible
    if legs < heads * 2 or legs > heads * 4 or legs % 2 == 1:
        return "Not possible"

    while heads != 0:

        if legs > heads * 3:
            heads -= 1
            legs -= 4
            rabbits += 1
        else:
            heads -= 1
            legs -= 2
            chickens += 1
    if legs < 0:
        return "Not possible"
    return rabbits, chickens


def count_rabbits_chickens2(heads, legs):
    rabbits = legs - 2 * heads
    if rabbits % 2:
        return "Not possible"
    else:
        rabbits //= 2
        chickens = heads - rabbits
        return rabbits, chickens


assert count_rabbits_chickens(100, 398) != count_rabbits_chickens(100, 398)
print(count_rabbits_chickens(88, 254))
print(count_rabbits_chickens(1, 1))
print(count_rabbits_chickens(1, 4))
print(count_rabbits_chickens(65, 166))
