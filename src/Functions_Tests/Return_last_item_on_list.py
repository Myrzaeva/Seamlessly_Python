def last_element(ls=[]):
    if len(ls) != 0:
        return ls[-1]
        return None


print(last_element([1, 2, 3]))
print(last_element())


def single_letter_count(str1="word", str2='o'):
    return tuple(str1.lower()).count(str2)


print(single_letter_count("Hello World", "h"))


def multiple_letter_count(s):
    return {key: s.count(key) for key in s}


print(multiple_letter_count("jay"))


def list_manipulation(a=[], b="", c="", d=0):
    if b == "remove" and c == "end":
        return a.pop()
    elif b == "remove" and c == "beginning":
        return a.pop(0)
    elif b == "add" and c == "beginning":
         a.insert(0, d)
         return a
    elif b == "add" and c == "end":
        a.append(d)
        return a


print(list_manipulation([1, 2, 3], "add", "end", 30))