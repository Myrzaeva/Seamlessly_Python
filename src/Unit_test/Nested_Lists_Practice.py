nested_1 = [[1, 3, 2, 3], [2, 3, 4, 4], [1, 2, 3]]
for each in nested_1:
    for x in each:
        print(f"each number in container {each} has the number {x}")

# Nested List Comprehension:
[[print(each) for each in first] for first in nested_1]

# Nested LC with using range():
# Create a new nested list:
board = [[num for num in range(1, 4)] for i in range(1, 5)]
print(board)

print([[f"{num} = even " if num % 2 == 0
        else f"{num} = odd" for num in range(1, 5)]
       for each_array in range(1, 6)])
