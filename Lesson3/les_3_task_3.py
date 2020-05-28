# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

a = [random.randint(-100, 100) for _ in range(10)]
print(a)

mn = 0
mx = 0

for i in range(1, len(a)):
    if a[i] < a[mn]:
        mn = i
    elif a[i] > a[mx]:
        mx = i

spam = a[mn]
a[mn] = a[mx]
a[mx] = spam

print(a)
