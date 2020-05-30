# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

a = [random.randint(-100, 100) for _ in range(10)]
print(a)

mn = 0
mx = 0

for i in range(len(a)):
    if a[i] < a[mn]:
        mn = i
    elif a[i] > a[mx]:
        mx = i

# spam = a[mn]
# a[mn] = a[mx]
# a[mx] = spam

a[mn], a[mx] = a[mx], a[mn]

print(a)

# Вариант 2
#
# min_num = min(a)
# max_num = max(a)
#
# idx_min = a.index(min_num)
# idx_max = a.index(max_num)
#
# a[idx_min], a[idx_max] = a[idx_max], a[idx_min]
#
# print(a)