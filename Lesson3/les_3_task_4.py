# 4. Определить, какое число в массиве встречается чаще всего.
import random

a = [random.randint(0, 10) for _ in range(20)]
print(a)

b = list(set(a))

c = [0] * len(b)

for i, item in enumerate(b):
    for j in a:
        if item == j:
            c[i] += 1

mx = -1
index = 0

for i, item in enumerate(c):
    if item > mx:
        mx = item
        index = i
print(f'Число {b[index]} встречается чаще всего: {mx} раза')
