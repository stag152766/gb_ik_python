# 4. Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 500
lst = [random.randint(0, 10) for _ in range(SIZE)]
print(lst)

lst = [6, 2, 8, 9, 5, 2, 8, 10, 0, 6, 3, 0, 2, 6, 10, 1, 0, 9, 8, 10]

# Вариант 1

def func_1(a):
    b = list(set(a))
    c = [0] * len(b)
    for i, item in enumerate(b):
        for j in a:
            if item == j:
                c[i] += 1
    mx = -1
    index = 0
    for i, item in enumerate(c):
        if item > mx:
            mx = item
            index = i
    return b[index]


# Вариант 2

def func_2(a):
    num = a[0]
    max_frq = 1
    for i in range(len(a) - 1):
        frq = 1
        for k in range(i + 1, len(a)):
            if a[i] == a[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = a[i]
    if max_frq > 1:
        return num
    else:
        return -1


# Вариант 3

def func_3(a):
    dict = {}
    for item in a:
        #  ключ = элемент, значение = частота
        if item in dict.keys():
            dict[item] += 1
        else:
            dict[item] = 1
    return dict


func_1(lst)
func_2(lst)
func_3(lst)

# len(list) = 10

# "les_4_task_1.func_1(lst)"
# 1000 loops, best of 5: 22.1 usec per loop

# "les_4_task_1.func_2(lst)"
# 1000 loops, best of 5: 55.9 usec per loop

# "les_4_task_1.func_3(lst)"
# 1000 loops, best of 5: 9.39 usec per loop


# len(lst) = 100

# "les_4_task_1.func_1(lst)"
# 1000 loops, best of 5: 94.8 usec per loop

# "les_4_task_1.func_2(lst)"
# 1000 loops, best of 5: 979 usec per loop

# "les_4_task_1.func_3(lst)"
# 1000 loops, best of 5: 45.3 usec per loop

# len(lst) = 500