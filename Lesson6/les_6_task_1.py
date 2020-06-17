# 1. Подсчитать, сколько было выделено памяти под переменные в
# программах, разработанных на первых трех уроках.
# Выберите 3 любые ваши программы для подсчёта.
import sys
from Lesson6.task_4 import show_size

print(sys.version, sys.platform)

# 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] win32


# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# Вариант 1
#   type=<class 'int'>, size=14, object=123
#  type=<class 'int'>, size=16, object=124231
#  type=<class 'int'>, size=14, object=1

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = int(input('Введите третье число: '))
#
# if (b < a < c) or (c < a < b):
#     print(f'Среднее число: {a}')
# elif (a < b < c) or (c < b < a):
#     print(f'Среднее число: {b}')
# else:
#     print(f'Среднее число: {c}')
#
# show_size(a)
# show_size(b)
# show_size(c)

# Вариант 2

#  type=<class 'list'>, size=44, object=[123, 124231, 1]
# 	 type=<class 'int'>, size=14, object=123
# 	 type=<class 'int'>, size=16, object=124231
# 	 type=<class 'int'>, size=14, object=1
#  type=<class 'int'>, size=14, object=1
#  type=<class 'int'>, size=16, object=124231

# print('Введите три натуральных числа: ')
# lst = [int(input()) for n in range(3)]
#
# max_num = max(lst)
# min_num = min(lst)
#
# for num in lst:
#     if num != max_num and num != min_num:
#         print(f'Среднее: {num}')
#
# show_size(lst)
# show_size(min_num)
# show_size(max_num)

# Вывод наиболее эффективная по использованию памяти программа в 1 варианте

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.


# Вариант 1
#  type=<class 'int'>, size=16, object=123456
#  type=<class 'str'>, size=26, object=6
#  type=<class 'str'>, size=27, object=65
#  type=<class 'str'>, size=28, object=654
#  type=<class 'str'>, size=29, object=6543
#  type=<class 'str'>, size=30, object=65432
#  type=<class 'str'>, size=31, object=654321
# Результат: 654321

# s = ''
# show_size(s)
#
# num = int(input('Введите число: '))
# show_size(num)
#
# while num != 0:
#     s += str(num % 10)
#     show_size(s)
#     num //= 10
# print(f'Результат: {s}')

# Вариант 2
#  type=<class 'list'>, size=52, object=['1', '2', '3', '4', '5', '6']
# 	 type=<class 'str'>, size=26, object=1
# 	 type=<class 'str'>, size=26, object=2
# 	 type=<class 'str'>, size=26, object=3
# 	 type=<class 'str'>, size=26, object=4
# 	 type=<class 'str'>, size=26, object=5
# 	 type=<class 'str'>, size=26, object=6
#  type=<class 'list'>, size=52, object=['6', '5', '4', '3', '2', '1']
# 	 type=<class 'str'>, size=26, object=6
# 	 type=<class 'str'>, size=26, object=5
# 	 type=<class 'str'>, size=26, object=4
# 	 type=<class 'str'>, size=26, object=3
# 	 type=<class 'str'>, size=26, object=2
# 	 type=<class 'str'>, size=26, object=1
#  type=<class 'str'>, size=31, object=654321

n1 = list(input('Введите целое число: '))
show_size(n1)
n1.reverse()
show_size(n1)
n2 = "".join(n1)
show_size(n2)
print(n2)

# Вывод наиболее эффективная по использованию памяти программа в 1 варианте


