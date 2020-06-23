# сортировка выбором О(n^2) в худшем, лучшем случае
import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def selecton_sort(array):
    for i in range(len(array)):
        idx_min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        # на каждой итерации внешнего цикла кладем
        # наименьший элемент неотсортированного массива
        # в начало неотсортированного массива
        array[idx_min], array[i] = array[i], array[idx_min]
        print(array)


selecton_sort(array)
print(array)
