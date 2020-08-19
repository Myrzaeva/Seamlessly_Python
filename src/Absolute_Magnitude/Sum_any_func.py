def sum_of_squares(n, func):
    i =0
    result = 0
    while i <= n:
        result += func(i)
        i += 1
    return result
def square(x):
    return x * x
print(sum_of_squares(10, square)) #285

def sum_of_squares(n):
    square_each = 0
    k , result = 0, 0
    while k <= n:
        square_each = k * k
        result += square_each
        k += 1
    return result
print(sum_of_squares(10))


def sum_square_shortest(n, k =0):
    return sum((k+(i*i)) for i in range(n+1) if k<=n)
print(sum_square_shortest(10))

