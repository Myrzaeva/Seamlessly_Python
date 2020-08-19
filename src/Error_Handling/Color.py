def colorize(text='', color=''):
    valid_color = ("cyan", "yellow", "white", "black")
    if type(text) is not str or color not in valid_color:
        raise TypeError(f"text must be instance of string "
                        f"or {color} is not from the "
                        f"list of valid_colors")
    print(f"{text} is of color {color}")


print(colorize("love", "blue"))



