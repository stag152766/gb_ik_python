"""
4. Найти сумму n элементов следующего ряда чисел:
 	1, -0.5, 0.25, -0.125, …
Количество элементов (n) вводится с клавиатуры.

"""


def func(n):
    if n != 0:
        i = 0
        s = [1]
        while i < (n - 1):
            s.append((s[i])/(-2))
            i += 1
        return sum(s)
    else:
        return 0

n = int(input('Введите n: '))
print(func(n))

