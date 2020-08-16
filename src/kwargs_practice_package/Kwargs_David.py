def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"
    return "Not sure who you are!"


print(special_greeting(HEather="hello", David="special"))


# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)


nums = [90, 1, 35, 67, 89, 20, 3, 1, 2, 3, 4, 5, 6, 9, 34, 46, 57, 68, 79, 12, 23, 34, 55, 1, 90, 54, 34, 76, 8, 23,
        34, 45, 56, 67, 78, 12, 23, 34, 45, 56, 67, 768, 23, 4, 5, 6, 7, 8, 9, 12, 34, 14, 15, 16, 17, 11, 7, 11, 8,
        4, 6, 2, 5, 8, 7, 10, 12, 13, 14, 15, 7, 8, 7, 7, 345, 23, 34, 45, 56, 67, 1, 7, 3, 6, 7, 2, 3, 4, 5, 6, 7,
        8, 9, 8, 7, 6, 5, 4, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 8, 7, 6, 5, 4, 3, 2, 1, 7]
result1 = count_sevens(7, 7, 8)
print(result1)
print(count_sevens(*nums))

# make_float, operation, message, first, second,
def calculate(**kwargs):
    if kwargs["operation"] == "add":
        if kwargs["make_float"]:
            return kwargs["message "].join(kwargs["first"]+kwargs["second"])
        else:
            return kwargs["The result is"].join(kwargs["first"]+kwargs["second"])
    elif kwargs["operation"] == "subtract":
        if kwargs["make_float"]:
            return kwargs["message "].join(float(kwargs["first"]-kwargs["second"]))
        else:
            return kwargs["The result is"].join(kwargs["first"]-kwargs["second"])
    elif kwargs["operation"] == "divide":
        if kwargs["make_float"]:
            return kwargs["message "].join(float(kwargs["first"]/kwargs["second"]))
        else:
            return kwargs["The result is"].join(kwargs["first"]/kwargs["second"])
    elif kwargs["operation"] == "multiply":
        if kwargs["make_float"]:
            return kwargs["message "].join(float(kwargs["first"]*kwargs["second"]))
        else:
            return kwargs["The result is"].join(kwargs["first"]*kwargs["second"])


print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))
