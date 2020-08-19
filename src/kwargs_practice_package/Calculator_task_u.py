# make_float, operation, message, first, second,
def calculate(make_float=False, operation='add',
              first=1, second=1, message="The result is", **kwargs):
    if operation == 'add':
        if make_float:
            return f"{message} {(float(first + second))}"
        return f"{message} {(int(first + second))}"
    if operation == 'divide':
        if make_float:
            return f"{message} {(float(first / second))}"
        return f"{message} {(int(first / second))}"
    if operation == 'subtract':
        if make_float:
            return f"{message} {(float(first - second))}"
        return f"{message} {(int(first - second))}"
    if operation == 'multiply':
        if make_float:
            return f"{message} {(float(first * second))}"
        return f"{message} {(int(first * second))}"


print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))


# 2nd way shorter
def calculate(**kwargs):
    calculation = {
        "add": kwargs.get("first", 0) + kwargs.get("second", 0),
        "subtract": kwargs.get("first", 0) - kwargs.get("second", 0),
        "divide": kwargs.get("first", 0) / kwargs.get("second", 0),
        "multiply": kwargs.get("first", 0) * kwargs.get("second", 0),
    }
    c = calculation[kwargs.get('operation', '')]
    r = kwargs.get('make_float', False)
    if r:
        return "{} {}".format(kwargs.get('message', 'The result is'), float(c))
    else:
        return "{} {}".format(kwargs.get('message', 'The result is'), int(c))


print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))
