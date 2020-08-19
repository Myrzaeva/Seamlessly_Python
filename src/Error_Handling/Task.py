def divide(one, two):
    # if type(one) is not int and float:
    #     return "Please provide two integers or floats"
    try:
        return one/two
    except ZeroDivisionError:
        print("Please do not divide by zero")
    except TypeError:
        print("Please provide two integers or floats")

print(divide(4, ''))

def divide(a,b):
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total

import keyword
def contains_keyword(*args):
    if any(k for k in args if keyword.iskeyword(k)):
        return True
    return False


print(contains_keyword("import", "goodbye"))