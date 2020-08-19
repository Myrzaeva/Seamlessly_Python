def testing_nested_lc(matrix):
    transposed = [[row[i] for row in matrix] for i in range(3)]
    print(transposed)


testing_nested_lc([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

def testing_nested_list_comprehension(l):
    return list(map(lambda i: map(lambda e: e, l), l))


print(testing_nested_list_comprehension([[1, 1, 1], [2, 2, 2], [3, 3, 3]]))