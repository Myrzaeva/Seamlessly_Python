# 1st function:
def say_hi():
    print("Hi!")


def calculate_the_age():
    age = input("How old are you: \n")
    age = int(age)
    if age <= 18:
        print(f"A child of {age} years old you are")
    elif age > 18 and age <= 21:
        print(f"Almost an Adult of {age} years old")
    else:
        print("100% Adult is here!")


def sing_happy_birthday():
    birthday_year = int(input("How old are you turning today? \n"))
    for x in range(birthday_year):
        print("Happy Birthday to you!" * x)


say_hi()
calculate_the_age()
sing_happy_birthday()