# chr(65) = A
# up until chr(90) = Z
# 1st way
import string
answer = dict(zip(range(65,90),string.ascii_lowercase, ))
print(answer)

#2nd way:
n2 = {i : chr(i) for i in range(65, 91)}
print(n2)
