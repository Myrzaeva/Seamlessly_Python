class Person:
    _name = ""
    _age = 0
    _date_of_birth = 0

    def __init__(self, name, age, date_of_birth):
        self._name = name
        self._age = age
        self._date_of_birth = date_of_birth

    def __hello__(self):
        return f"hello {self._name}"

user1 = Person("Bora", 26, 1994)
print(user1._name + f" {user1._age} {user1._date_of_birth}")
print(user1.__hello__())
