def words_starting_with(lst, letter):
    return list(filter(lambda e: e[0].lower() == letter, lst))


# Task filter each item in the list by first letter which is 'b'

print(words_starting_with(["Bora", "Daria", "Masha", "Dhas", "Bermet", "Burul"], 'b'))