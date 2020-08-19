from time import time
from functools import wraps
start_time = time()
sum([x for x in range(100)])
total_time = time() - start_time
print(f"it took :{total_time}")

start_time = time()
sum(x for x in range(100))
total_time = time() - start_time

'''2nd way of Defining a speed test decorator:'''
'''Note from Zhibekchach: this is not the most accurate way of speed testing or benchmarking.
This is mostly to see how Java transitions into Python'''
def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        end_time = time()
        print(f"Time Elapsed : {end_time -start_time}")
        return result
    return wrapper

@speed_test
def sum_nums():
    return sum(x for x in range(1000000))


print(sum_nums())