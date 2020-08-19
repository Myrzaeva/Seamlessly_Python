from copy import copy
class Human:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"It is {self.first} {self.last} who is {self.age} y.o."

    def __add__(self, other):
        if isinstance(other, Human):
            return f"{Human(first = 'Newborn', last = 'baby', age = 0)} now"
        return TypeError("Not a Human!")

    def __mul__(self, other):
        if isinstance(other, int):
            return f"You wanna multiply {self.first}!" \
                   f" Here we go:\n{[copy(self) for e in range(other)]}"
        return TypeError(f"Enter number instead of person : \'{other}\'")


woman = Human("Larson", "Li", 26)
man = Human("London", "Kay", 37)
print(woman)
print(man)
print(woman.__add__(man))
print(woman+man)
print(woman * 4)
print(woman*man)
