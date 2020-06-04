# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
import random
import cProfile


def max_below_zero(size):
    # SIZE = 10
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    # print(array)

    i = 0
    index = -1

    while i < size:
        if array[i] < 0 and index == -1:
            index = i
        elif array[i] < 0 and array[i] > array[index]:
            index = i
        i += 1
    # print(f'Число {array[index]} на позиции {index}')
    return f'Число {array[index]} на позиции {index}'

# "hw_4_task_1.max_below_zero(10)"
# 1000 loops, best of 5: 40.3 usec per loop

# "hw_4_task_1.max_below_zero(100)"
# 1000 loops, best of 5: 361 usec per loop

cProfile.run('max_below_zero(1000)')


# Documents/GitHub/gb_ik_python/Lesson4/hw_4_task_1.py
#          58 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 hw_4_task_1.py:7(max_below_zero)
#         1    0.000    0.000    0.000    0.000 hw_4_task_1.py:9(<listcomp>)
#        10    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:218(randint)
#        10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# /hw_4_task_1.py
#          5629 function calls in 0.006 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#         1    0.000    0.000    0.006    0.006 hw_4_task_1.py:7(max_below_zero)
#         1    0.001    0.001    0.006    0.006 hw_4_task_1.py:9(<listcomp>)
#      1000    0.002    0.000    0.004    0.000 random.py:174(randrange)
#      1000    0.001    0.000    0.005    0.000 random.py:218(randint)
#      1000    0.002    0.000    0.003    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1624    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}