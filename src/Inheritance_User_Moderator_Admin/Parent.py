class Mother:
    def eat(self, food):
        print(food)

    cool = True


class Child(Mother):
    pass


docha = Child()
docha.eat("okroshka")
print(docha.cool)
