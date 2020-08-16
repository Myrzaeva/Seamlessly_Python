def calculate_2_nums(one, two):
    choose = input("What do you want?\nMultiply\nDivide\nSubtract\nAdd \n")
    i = 0
    while i >= 0:
        if choose.lower() == "multiply":
            print(one * two)
        elif choose.lower() == "divide":
            print(one / two)
        elif choose.lower() == "subtract":
            print(one - two)
        elif choose.lower() == "add":
            print(one + two)
        else:
            return "invalid entry"
        answer = input("Are you happy with this calculator? \n")
        secondQ = input("Another operations? \n")
        if secondQ == "yes" or answer == "yes":
            i = 0;
            choose = input("What do you want?\nMultiply\nDivide\nSubtract\nAdd \n")
        else:
            i = -1

# let's run the calculate_2_nums():
print(calculate_2_nums(2, 6))
