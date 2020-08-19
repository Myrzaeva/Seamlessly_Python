# only matching data from two lists:
def intersection(l1=[], l2=[]):
    l3 = list(set(l1).intersection(l2))
    return l3


print(intersection(["Jay", "Bora"], ["Daria", "Bora"]))

