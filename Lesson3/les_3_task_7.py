# 7. В одномерном массиве целых чисел определить два
# наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.
import random

a = [random.randint(-100, 100) for _ in range(10)]
print(a)

mn = 0

for i in range(1, len(a)):
    if a[i] < a[mn]:
        mn = i
print(f'первый минимальный : {a[mn]}')

b = a[:mn] + a[mn + 1:]

mn_b = 0
for i in range(1, len(b)):
    if b[i] < b[mn_b]:
        mn_b = i

print(f'второй минимальный: {b[mn_b]}')
