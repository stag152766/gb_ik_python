"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
Пример: 4
		8
		15469
        5648
        165489
        6161
"""

a = int(input("Введите количество чисел: "))
n = int(input("Введите число, которое нужно посчитать: "))
r = 0

while a > 0:
    a -= 1
    s = int(input("Введите число последовательности: "))
    while s > 0:
        if s % 10 == n:
            r +=1
        s //= 10
print(r)