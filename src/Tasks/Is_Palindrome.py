def is_palindrome(w=""):
    no_space = [e.lower() for e in w if e != " "]
    first_copy = no_space.copy()
    second_copy = first_copy[::-1]
    return first_copy == second_copy


print(is_palindrome("test ing"))
