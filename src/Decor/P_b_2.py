def standardize(fn):
    def plans():
        print("Standard plan check")
        fn()
        print("Execution is done")
    return plans

def premium():
    print("Premium customers")

@standardize
def greet():
    print(f"Interest rate is 5.5%")

greet()



