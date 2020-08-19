
person = [["name", "Jared"], ["job", "Musician"],
          ["city", "Bern"]]
# 1 way:
answer = {e[0] : e[1]for e in person}
print(answer)
# 2 way:
another_dict = dict(person)
print(another_dict)
# 3 way:
third_dict = {each[0] : each[1] for each in person}
print(third_dict)
# 4 way:
fourth_dict = {k : y for k, y in person}
print(fourth_dict)
