# 6. В одномерном массиве найти сумму элементов, находящихся
# между минимальным и максимальным элементами. Их самих в
# сумму не включать.
import random

a = [random.randint(-100, 100) for _ in range(10)]
print(a)

mx = 0
mn = 0

for i in range(1, len(a)):
    if a[i] < a[mn]:
        mn = i
    elif a[i] > a[mx]:
        mx = i

sum = 0

if mx > mn:
    b = a[mn + 1:mx]
    for i in b:
        sum += i

elif mn > mx:
    b = a[mx + 1:mn]
    for i in b:
        sum += i
print(f'Ответ: {sum}')
