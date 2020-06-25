# Разворот массива

import random

size = 10
array = [i for i in range(10)]
random.shuffle(array)
print(array)


def revers(array):
    for i in range(len(array) // 2):
        # меняем зеркально расположенные элементы
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]


revers(array)
print(array)

array.reverse()
print(array)

array.sort(reverse=True)
print(array)

print('*' * 50)
t = tuple(random.randint(0,100) for _ in range(10))
print(t)

# кортеж неизменяемая структура
#t.sort()

# есть специальная функция
t = tuple(sorted(t, reverse=True))
print(t)


