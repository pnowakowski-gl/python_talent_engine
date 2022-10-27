def is_anagram(str1, str2):
    str1, str2 = str1.lower(), list(str2.lower())
    if len(str1) == len(str2):
        for i in range(len(str2)):
            if str1[i] in str2:
                str2.remove(str1[i])
            else:
                return False
    else:
        return False
    return True
    
print(is_anagram("AbbA", "BBaA"))  #True
print(is_anagram("Good", "gooOD"))  #False
print(is_anagram("AAABB", "AABBB"))  #False

