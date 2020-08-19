class One:
    def __init__(self):
        pass
    def __repr__(self):
        return f"{self.name} is {self.age} years old!"

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new_name):
        self.name = new_name

    @property
    def age (self):
        return self.age

    @age.setter
    def age(self, new_age):
        self.age = new_age


o1 = One()
o1.age = 26
o1.name = "Bora"
print(o1.name)
print(o1.age)
