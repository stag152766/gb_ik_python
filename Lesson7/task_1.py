# сортировка пузырьком О(n^2)
import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


n = 1 # счетчик , виток сортировки

while n < len(array):
    for i in range(len(array)- n):
        if array[i]> array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
        print(array, i, n)
    n += 1
print(array)
