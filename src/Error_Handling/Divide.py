def divide(a, b ):
    try:
        return a/b
    except ZeroDivisionError:
        print("Mistake!")
    except TypeError:
        print("Input a number")


print(divide(1, 0))
print(divide('a', 0))
