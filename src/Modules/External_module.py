# let's practice on termcolor:
import sys
import math
import autopep8
import pyfiglet
from termcolor import colored

text = colored("Hi There", color="red", on_color="on_green", attrs=["blink"])
print(text)

# pyfiglet :

print(pyfiglet.COLOR_CODES)
print(pyfiglet.print_function)
help(pyfiglet)

result = pyfiglet.figlet_format("hi")
print(result)

# to colorize:
msg = input("What would you like to print?")
color = input("What color?")
ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color=color)
print(ascii_art)

# autopep8 to format the ocde and solve indentation issues!


def example():
    s_tuple = 1, 2, 3, 'g'
    s_variable = {'long': 'Long code'}
    is_owner = True
    if is_owner:
        print("True")

    return (s_tuple, s_variable)
