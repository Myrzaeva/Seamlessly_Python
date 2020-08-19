# Immutable data structure!
alphabet = ('a', 'b', 'c', 'd')
# will not print cause it is a tuple
# you have to cast it
print(tuple(alphabet))

# to declare a tuple just put data in parentheses:
months = ("January", "February", "March", "April", "May",
          "June", "July", "August", "September",
          "October", "November", "December")
locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "San Francisco Office"
}
# so here we can map through the collection
# by using tuples as keys:
print(locations[(35.6895, 39.6917)])

# Looping : for loop!
for gps in locations.values():
    print(gps)

# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1,2,3,4)
print(numbers)
# 2 - Create a variable called value which is a tuple with the the value 1 inside.

value = tuple(1)
# 3 - Given the following variable:
print(value)
values = [10,20,30]

# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)
print(static_values)
# 4 - Given the following variable

stuff = [1,3,1,5,2,5,1,2,5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)