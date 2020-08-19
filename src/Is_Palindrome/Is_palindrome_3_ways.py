def check_if_palindrome(s = "Aboba"):
    return s.lower() == s[::-1].lower()
print(check_if_palindrome("aboba"))#True


def check_if_palindrome_2_way(s = "Abo ba"):
    first_list = [i.lower() for i in s if i != " "]
    second_list = first_list[::-1]
    return first_list == second_list
print(check_if_palindrome_2_way('ab o b a')) #True
print(check_if_palindrome_2_way('ab o a')) # False

