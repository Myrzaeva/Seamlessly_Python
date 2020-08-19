def function(l):
    return list(map(lambda e: e - 1, l))


print(function([1, 33, 44, 556]))


def are_evens(l):
    return list(filter(lambda i: i % 2 == 0, l))
    # [2, 4, 66464, 3242, 32]


print(are_evens([2, 3, 4, 5, 66464, 3242, 11, 32, 7677]))
# <filter object at 0x7fdeb2070430>
