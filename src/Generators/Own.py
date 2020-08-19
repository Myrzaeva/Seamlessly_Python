def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


counter = count_up_to(5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))



def yes_or_no_gener():
    answer = "yes"
    while True:
        yield answer
        if  answer == "yes":
            answer = "no"
        else:
            answer = "yes"

c = yes_or_no_gener()
print(next(c))
print(next(c))
print(next(c))