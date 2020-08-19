def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}"

@shout
def order(one, two):
    return f"for one {one} , for two is {two}"

print(greet("B237"))
print(order("burger", "fries"))