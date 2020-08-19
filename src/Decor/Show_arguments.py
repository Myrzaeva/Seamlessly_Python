from functools import wraps


def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper


@show_args
def do_nothing(*args, **kwargs):
    print(e for e in args)
    print(dict(e for e in kwargs.items()))


print(do_nothing(1, 2, 3, a='hi', b='bye'))

'''Shorter way:'''
def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)

    return wrapper


print(do_nothing(1, 2, 3, a='hi', b='bye'))
