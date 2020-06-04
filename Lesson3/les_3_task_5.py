# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
import random

SIZE = 10
a = [random.randint(-100, 100) for _ in range(SIZE)]
print(a)

# вариант 1
mn = float('-inf')
index = -1

for i, item in enumerate(a):
    if 0 > item > mn:
        mn = item
        index = i
print(f'Число: {mn} на позиции {index}')

# вариант 2
i = 0
index = -1

while i < SIZE:
    if a[i] < 0 and index == -1:
        index = i
    elif a[i] < 0 and a[i] > a[index]:
        index = i
    i += 1
print(f'Число {a[index]} на позиции {index}')

