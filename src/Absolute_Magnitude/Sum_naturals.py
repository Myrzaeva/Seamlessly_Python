def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total = ((n+1)*n)/2
        return total


def square(x):
    return x * x


print(sum_naturals(10))
