def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive"
    return x+y


add_positive_numbers(1,1)



def eat_junk(food):
    assert food in ['pizza', 'ice-cream'], 'you eat healthy'

food = input("Enter a food please")
print(eat_junk(food))