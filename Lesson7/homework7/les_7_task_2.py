# 2. Отсортируйте по возрастанию методом слияния одномерный
# вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и
# отсортированный массивы.

import random

array = [round(random.uniform(0, 50), 2) for i in range(0, 50)]
random.shuffle(array)
print(array)


def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        left = array[:len(array) // 2]
        right = array[len(array) // 2:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:] + right[j:]
    return result


s = merge_sort(array)
print(s)
