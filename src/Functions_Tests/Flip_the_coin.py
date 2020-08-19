from random import random
import numpy


# module that comes from python
def flip_coin():
    if random() > 0.5:
        return "Heads"
    else:
        return "Tales"


print(flip_coin())


# to override just make another kind of the function,
# interpreter will understand
def flip_coin():
    if random() > 0.5:
        return "HEADS"
    else:
        return "TALES"


print(flip_coin())


# return evens:
def generate_evens():
    s = 0
    [i for i in range(1, 50) if i % 2 == 0]

    return s


print(generate_evens())


# return squared number:
def square_num(num):
    return num ** 2


print(square_num(56))


# Multiply contents of List:
# 1st try:
def multiply_even_numbers(a=[]):
    for e in a:
        if e % 2 == 0:
            result = numpy.prod(e)
    return result


print(multiply_even_numbers([1, 3, 4, 80, 9]))


# 2nd try:
def multiply_even_numbers(a=[]):
    result = 1
    for i in a:
        if i % 2 == 0:
            result = result * i
    return result


print(multiply_even_numbers([1, 3, 4, 80, 9]))


# 3rd
def compact(a=[]):
    res = []
    for i in a:
        if i:
            res.append(i)

    return res


print(compact([1, 2, [], False, {}, None, "All done"]))
