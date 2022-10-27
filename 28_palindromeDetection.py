def is_palindrome(s):
    str_ = [i.lower() for i in s if i.isalpha()]
    return str_ == str_[::-1]
    
print(is_palindrome("racecar")) # True
print(is_palindrome("Race Car")) # True
print(is_palindrome("A man, a plan, a canal, Panama!"))  # True
                                    