# using Dictionary Comprehension

def create_dict(l1, l2, l3):
    return {e[0]: max(e[1], e[2]) for e in zip(l1, l2, l3)}


print(create_dict([1, 2, 3], [4, 5, 6], [6, 7, 8]))
