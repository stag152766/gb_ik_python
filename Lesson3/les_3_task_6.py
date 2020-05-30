# 6. В одномерном массиве найти сумму элементов, находящихся
# между минимальным и максимальным элементами. Их самих в
# сумму не включать.
import random

SIZE = 10
a = [random.randint(-100, 100) for _ in range(SIZE)]
print(a)

mx = 0
mn = 0

for i in range(1, SIZE):
    if a[i] < a[mn]:
        mn = i
    elif a[i] > a[mx]:
        mx = i

if mn > mx:
    a[mn], a[mx] = a[mx], a[mn]

sum = 0

for i in range(mn + 1,mx):
    sum += a[i]

print(f'Ответ: {sum}')
