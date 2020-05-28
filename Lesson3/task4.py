# 2. Вставка элемента в произвольное место массива
import random

array = [random.randint(-100,100) for _ in range(100)]
print(array)


num =int(input('Введите целое число для вставки: '))
pos = int(input('На какую позицию вставить число: '))

# array.append(None)
#
# # переменная которая указывает какие элементы должны поменять
# # изначально указывает на None
# i = len(array) - 1
#
# # попарно меняет элементы
# while i > pos:
#     array[i], array[i -1] = array[i-1], array[i]
#     i -= 1

#array.insert(pos,num)

array[pos] = num

# способ 2
# создание нового списка через срезы

new_array = array[pos:] + [num] + array[:pos]

print(array)
