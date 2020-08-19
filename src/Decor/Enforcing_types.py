def enforce_types(*types):
    def decorator(fn):
        def new_func(*args, **kwargs):
            newargs = []
            for (a, b) in zip(args, types):
                newargs.append(b(a))
            return fn(*newargs, **kwargs)
        return new_func
    return decorator



@enforce_types(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

@enforce_types(float,float)
def divide(n1, n2):
    return (n1 /n2)

repeat_msg("Seamlessly icon", '3')
print(divide('3', 23))
