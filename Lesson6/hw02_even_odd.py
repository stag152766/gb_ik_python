# 2. Посчитать четные и нечетные цифры введенного натурального числа.
#Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
from Lesson6 import sum_memory


o = []
e = []
num = int(input('Введите натуральное число: '))
while num != 0:
    r = num % 10 % 2
    num = num // 10
    if r == 0:
        e.append(r)
    else:
        o.append(r)
print(f'Четных {len(e)}, нечетных {len(o)}')

sum_mem =sum_memory.SumMemory()
sum_mem.extend(num,r,o,e)
sum_mem.print_sum()