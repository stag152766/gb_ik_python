# сортировка вставками
# О(n^2) в лучшем O(n)
import random

# size = 10
# array = [i for i in range(size)]
# random.shuffle(array)
# print(array)
array = [1,3,8,6,0,5]

def insertion_sort(array):
    for i in range(len(array)):
        spam = array[i]
        j = i

        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1
            print(f'\t\t{array},')
        array[j] = spam
        print(array)

insertion_sort(array)
print(array)