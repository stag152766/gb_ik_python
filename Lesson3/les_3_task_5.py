# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

a = [random.randint(-100,100) for _ in range(20)]
print(a)

mn = -9999999
index = 0
for i, item in enumerate(a):
    if item < 0 and item > mn:
        mn = item
        index = i
print(f'{index}:{mn}')