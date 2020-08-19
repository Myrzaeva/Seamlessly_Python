from functools import wraps
def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"video call to {fn.__name__}")
        print(f"documentation : {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def collect_data(x,y):
    '''the approximate collection of data is stored in PostgreSQL'''
    return x+y


print(collect_data(100, 43627452))
print(collect_data.__doc__)
print(collect_data.__name__)
