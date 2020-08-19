def standardize(fn):
    def plans():
        print("Standard plan check")
        fn()
        print("Execution is done")
    return plans

def premium():
    print("Premium customers")

greet = standardize(premium)
greet()



