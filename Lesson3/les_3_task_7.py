# 7. В одномерном массиве целых чисел определить два
# наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.
import random

SIZE = 10
a = [random.randint(-100, 100) for _ in range(SIZE)]
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

# Вариант 2

# Предположим, что двумя наименьшими элементами массива являются первый и второй элемент.
if a[0] > a[1]:
    min_idx_1 = 0
    min_idx_2 = 1
else:
    min_idx_1 = 1
    min_idx_2 = 0

for i in range(2, SIZE):
    if a[i] < a[min_idx_1]:
        spam = min_idx_1
        min_idx_1 = i

        if a[spam] < a[min_idx_2]:
            min_idx_2 = spam

    elif a[i] < a[min_idx_2]:
        min_idx_2 = i
print(f'Число {a[min_idx_1]} в ячейке {min_idx_1}')
print(f'Число {a[min_idx_2]} в ячейке {min_idx_2}')
