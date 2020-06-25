# 1. Отсортировать по убыванию методом «пузырька» одномерный
# целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Вывести на экран исходный и
# отсортированный массивы.
import random

array = [i for i in range(-100, 100)]
random.shuffle(array)
print(array)



def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n +=1

bubble_sort(array)
print(array)