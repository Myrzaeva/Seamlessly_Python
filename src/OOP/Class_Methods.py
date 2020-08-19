class Person:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    @classmethod
    def display_active_users(cls):
        # cls signifies that this is actual class:
        print(cls)

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, age)


p1 = Person
print(p1.display_active_users())

p2 = Person.from_string("Tom,Jones,90")
print(p2.first)
print(p2.last)
print(p2.age)
