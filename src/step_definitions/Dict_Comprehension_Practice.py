# dict of vowels only
# 1st way:
answer = {}.fromkeys("aeiou",0)
print(answer)

p = dict.fromkeys("aeiou",0)
print(p)

c = {a : 0 for a in "aeiou"}
print(c)