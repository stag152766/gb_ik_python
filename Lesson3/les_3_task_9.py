# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

SIZE = 5

matrix = [[random.randint(0, 100) for _ in range(SIZE)] for _ in range(SIZE)]

for line in matrix:
    print(line)
print()

mx = -1

for j in range(SIZE):
    mn = 99999999
    for i in range(SIZE):
        if matrix[i][j] < mn:
            mn = matrix[i][j]
    if mn > mx:
        mx = mn
print(f'Ответ: {mx}')
