# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

m = 5
n = 5

matrix = [[random.randint(0, 100) for _ in range(m)] for _ in range(n)]

for line in matrix:
    print(line)
print('-' * len(matrix) * 5)

mx = -1

for j in range(m):
    mn = 99999999
    for i in range(n):
        if matrix[i][j] < mn:
            mn = matrix[i][j]
    if mn > mx:
        mx = mn
print(mx)
