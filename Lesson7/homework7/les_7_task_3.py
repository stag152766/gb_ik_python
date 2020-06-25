# 3. Массив размером 2m + 1, где m – натуральное число, заполнен
# случайным образом. Найти в массиве медиану – элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы.

from collections import Counter
import random
import math

m = 5
size = 2 * m + 1
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def get_median(array):
    c = Counter(array)

    median = len(array) // 2 + 1
    n = 0
    median_value = 0

    while n < median:
        min = math.inf
        for k, v in c.items():
            if k < min:
                min = k
        n += c[min]
        median_value = min
        c.pop(min)

    return median_value


median = get_median(array)
print(f'Медиана массива равна: {median}')