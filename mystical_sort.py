import re

SEPARATORS = ",;|\t"
test_string = "boom;dracula,apple|coca-cola|fate|Love and other stuff\tZoomba-yumba"


def test_me(s=test_string):
    separators = ""
    for sep in SEPARATORS:
        if sep != "|":
            separators += sep + "|"
        else:
            separators += "\\" + sep + "|"
    separators = separators[:-1]
    m_sort = sorted(re.split(separators, s), key=str.casefold)
    return ",".join(m_sort)


print(test_me())
