def get_multiples(number= 1, count=10):
    num = number
    while count > 0:
        yield num
        count -= 1
        num += number


print(next(get_multiples(2, 3)))
print(next(get_multiples(2, 3)))
print(next(get_multiples(2, 3)))

'''
sevens = get_unlimited_multiples(7)
[next(sevens) for i in range(15)] 
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
[next(ones) for i in range(20)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''
def get_unlimited_multiples(number = 1):
    n = number
    while number > 0:
        yield n
        n += number


ones = get_unlimited_multiples(7)
print([next(ones) for i in range(20)])




