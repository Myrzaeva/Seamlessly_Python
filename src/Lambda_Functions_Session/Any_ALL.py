def is_all_string(l):
    return all([type(i) ==str for i in l])

# test it:

print(is_all_string(["J", ""]))
