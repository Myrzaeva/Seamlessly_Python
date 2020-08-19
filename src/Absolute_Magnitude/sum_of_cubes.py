def sum_of_cubes(n):
    k, cubed = 1, 0
    while k <= n:
        cubed = (((n + 1) * n) / 2)
        cubed = cubed * cubed
        return cubed


print(sum_of_cubes(4)) # 100