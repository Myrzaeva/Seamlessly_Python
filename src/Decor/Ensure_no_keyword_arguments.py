from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed!")
        return fn(*args, **kwargs)
    return wrapper

@ensure_no_kwargs
def make_a_payment(section):
    print(f"payment is made for {section}")


print(make_a_payment(name = "American Eagles"))