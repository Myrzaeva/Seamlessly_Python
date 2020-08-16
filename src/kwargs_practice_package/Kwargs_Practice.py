def let_s_practice_kwargs(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s fav color is {color}")


# keyword args
let_s_practice_kwargs(colt="purple", jay="white", bora="yellow")
