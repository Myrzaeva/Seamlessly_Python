# using Dictionary Comprehension

def create_dict(l1, l2, l3):
    return {e[0]: (e[1], e[2]) for e in zip(l1, l2, l3)}


print(create_dict([1, 2, 3], [4, 5, 6], [6, 7, 8]))

# using Dictionary Comprehension in 2nd way:
clients = ["Standard", "Premium", "Golden"]
spending_rate = [83724, 64728, 3822]
entry_year = [1999, 2010, 2019]
print(dict(zip(clients, (y for y in zip(spending_rate, entry_year)))))

# using lambda:
clients = ["A", "B", "C"]
spending_rate = [83724, 64728, 3822]
entry_year = [1999, 2010, 2019]
analyzes = dict(
    zip(
        clients,
        map(
            lambda x: x,
            zip(spending_rate, entry_year)
        )
    )
)
print(analyzes)


def create_new_dict(l1):
    return dict({i for i in e} for e in list(l1))


person = [["name", "Jared"],["job", "Musician"],["city", "Bishkek"]]
print(create_new_dict(person))


def create_dict_using_lambda(l1):
    return {a[0]: b for a in person for b in a[1::]}


print(create_dict_using_lambda(person))