# fromkeys() with string:
some_container = {}.fromkeys("love", "python")
print(some_container)

# fromkeys() with range()

range_container = {}.fromkeys(range(1, 4), "Bora")
print(range_container)

# pop() removes key-value pair based on key:
# but it returns the value of removed item:
dictionary_1 = dict(one=32, two="love", three="family")
print(dictionary_1.pop("three")) # removes "family" and
# returns it as proof
print(dictionary_1)

# popitem() removes any key:
print(dictionary_1.popitem())
# it removed 'two':'love'
print(dictionary_1)

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
print(inventory)
stock_list = inventory.copy()
print(stock_list)
stock_list["cookie"]=18
print(stock_list["cookie"])
stock_list.pop("bagel")
print(stock_list)