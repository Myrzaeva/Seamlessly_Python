def list_of_fib(max):

    a, b = 0, 1
    count = []
    while len(count) < max:
        a, b = b, a+b
        count.append(a)
    return count


for i in list_of_fib(100000):
    print(i)


