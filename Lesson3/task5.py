import random

matrix = [[random.randint(1,10) for _ in range(5)] for _ in range(7)]

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()


# 1. Посчитать сумму строк и столбцов матрицы

# отдельный список который будет считать сумму по строке
sum_column = [0] * len(matrix[0])

for line in matrix:
    sum_line = 0
    # номер столбца i , значение элемента item
    for i, item in enumerate(line):
        sum_line += item
        sum_column[i] += item
        print(f'{item: > 5}', end='')
    print(f'   | {sum_line}')

print('-' * len(matrix) * 4)

for s in sum_column:
    print(f'{s: > 5}', end='')

# 2. Обмен значений главной и побочной диагоналей квадратной матрицы


