"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести 6843.

"""

s = ''
num = int(input('Введите число: '))

while num != 0:
    s += str(num % 10)
    num //= 10
print(f'Результат: {s}')
