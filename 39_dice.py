# The following three constant definitions are equal.
# But the first(which looks the best) doesn't work
#   in CodeRunner
# DICES = "⚀⚁⚂⚃⚄⚅"
# DICES = "\N{DIE FACE-1}\N{DIE FACE-2}\N{DIE FACE-3}" \
#        "\N{DIE FACE-4}\N{DIE FACE-5}\N{DIE FACE-6}"
from random import randint

DICES = "\u2680\u2681\u2682\u2683\u2684\u2685"


def dice(number=1):
    roll_the_dice = randint(0, 5)
    return " ".join([DICES[randint(0, 5)] for _ in range(number)])


# Some basic tests
print(f"All dices are: {DICES}")
print(dice())  # Should be some dice outputted
print(dice(3))  # Should be 3 dice outputted
print(dice(3).count(" ") == 2 and len(dice(3)) == 5)  # Should be True
print(all(x in DICES for x in dice(3).replace(" ", "")))  # Should be True
