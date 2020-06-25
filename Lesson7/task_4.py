import random

# size = 10
# array = [i for i in range(size)]
# random.shuffle(array)
# print(array)
array = [9, 5, 1, 0, 3, 8, 4, 7, 2, 6]

def shell_sort(array):
    assert len(array) < 4000, 'Массив слишком большой. Используйте другую сортировку'

    # генератор
    # как хранить и получать шаг
    def new_increment(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]

        while len(array) <= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()

    # внешний цикл для получения значение приращения
    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
                print(array)


shell_sort(array)
print(array)
