from functools import wraps
from time import sleep


def delay(n):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args):
            print(f"Waiting {n}s before running say_hi")
            sleep(n)
            return fn(*args)
        return wrapper
    return inner

@delay(3)
def say_hi():
     return "hi"


print(say_hi())
