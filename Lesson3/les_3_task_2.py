# 2.Во втором массиве сохранить индексы четных элементов первого массива.
import random

a = [random.randint(0, 20) for _ in range(10)]
print(a)
b = []

for i, item in enumerate(a):
    if item % 2 == 0:
        b.append(i)
print(b)
