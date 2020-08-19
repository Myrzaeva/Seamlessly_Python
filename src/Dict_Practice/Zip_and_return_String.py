def interleave(one, two):
    return "".join(i + j for i, j in zip(one, two)).lower()

print(interleave("HI", "you"))