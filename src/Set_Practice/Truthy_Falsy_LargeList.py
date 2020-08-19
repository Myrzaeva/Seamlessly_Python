
def partition(l, fn):
    truthy = []
    falsy = []
    for i in l:
        if fn(i): # if True value
            truthy.append(i)
        else:
            falsy.append(i)

    return [truthy,falsy]


print(partition(["Love", 1, 2, True, False], bool))


def contains_purple(*args):
    if "purple" in args:
        return True
    return False


print(contains_purple("Life", "is", "purple")) # True!