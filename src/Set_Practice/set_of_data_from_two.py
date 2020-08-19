def intersection_using_set(l1, l2):
    return [e for e in set(l1+l2)]


print(intersection_using_set([1, 2, 3], [2, 3, 4]))


def reverse_str(name):

    i = len(name) -1
    reversed_word =""
    while i >= 0:
        reversed_word += name[i]
        i -=1

    return reversed_word


print(reverse_str("Gulbara"))


def reversing_list(l):
    return l[::-1]

print(reversing_list([1, 2, 3, 4]))


def reversing_with_stepbacksclicing(n):
    return n[::-1]


print(reversing_with_stepbacksclicing("Boraks"))



