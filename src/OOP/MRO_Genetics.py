# Define your classes below:
class Mother:
    def __init__(self, eye_color="brown", hair_color="dark brown", hair_type="curly"):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type

    def __repr__(self):
        return self.eye_color + " " + self.hair_color


class Father:
    def __init__(self, eye_color="blue", hair_color="blond", hair_type="straight"):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type

    def __repr__(self):
        return self.eye_color + " "+ self.hair_color


class Child(Mother, Father):
    pass


c = Child()
print(c)