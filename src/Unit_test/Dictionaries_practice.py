cat = {"name": "blue", "age": 3.5, "isCute": True}
cat2 = dict(cat)
print(cat)  # {'name': 'blue', 'age': 3.5, 'isCute': True}
print(cat2)  # {'name': 'blue', 'age': 3.5, 'isCute': True}
cat3 = dict(score=20, name='Aliya')
print(cat3)

print(cat3['score'])
artist = {
    "first": "Neil",
    "last": "Young",
}
