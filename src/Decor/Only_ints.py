from functools import wraps


def only_ints(fn):
    @wraps(fn)
    def wrapper(*args):
        for e in args:
            if type(e) == int:
                return fn(*args)
            return "Please only invoke with integers."
    return wrapper

'''or use any()'''

def only_int(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return inner

@only_ints
def add(x, y):
    return x + y


print(add('1', '2'))
