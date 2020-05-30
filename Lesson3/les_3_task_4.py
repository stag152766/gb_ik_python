# 4. Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 20
a = [random.randint(0, 10) for _ in range(SIZE)]
print(a)
#
# b = list(set(a))
#
# c = [0] * len(b)
#
# for i, item in enumerate(b):
#     for j in a:
#         if item == j:
#             c[i] += 1
#
# mx = -1
# index = 0
#
# for i, item in enumerate(c):
#     if item > mx:
#         mx = item
#         index = i
# print(f'Число {b[index]} встречается чаще всего: {mx} раза')


# Вариант 2

num = a[0]
max_frq = 1

for i in range(SIZE - 1):
    frq = 1

    for k in range(i + 1, SIZE):
        if a[i] == a[k]:
            frq += 1

    if frq > max_frq:
        max_frq = frq
        num = a[i]

if max_frq > 1:
    print(f'Число {num} встречается {max_frq} раз')
else:
    print(f'Все элементы уникальны')

# Вариант 3
dict = {}
for item in a:
    #  ключ = элемент, значение = частота
    if item in dict.keys():
        dict[item] += 1
    else:
        dict[item] = 1
print(dict)
