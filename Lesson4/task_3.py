import cProfile
import functools


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# test_fib(fib)

# C:\Users\Admin\Documents\GitHub\gb_ik_python\Lesson4>python -m timeit -n 1000 -s "import task_3" "task_3.fib(10)"
# 1000 loops, best of 5: 44.1 usec per loop

# C:\Users\Admin\Documents\GitHub\gb_ik_python\Lesson4>python -m timeit -n 1000 -s "import task_3" "task_3.fib(15)"
# 1000 loops, best of 5: 675 usec per loop

# C:\Users\Admin\Documents\GitHub\gb_ik_python\Lesson4>python -m timeit -n 1000 -s "import task_3" "task_3.fib(20)"
# 1000 loops, best of 5: 6.99 msec per loop

cProfile.run('fib(100)')
# 177/1    0.000    0.000    0.000    0.000 task_3.py:10(fib)

# 1973/1    0.002    0.000    0.002    0.002 task_3.py:10(fib)

# 21891/1    0.036    0.000    0.036    0.036 task_3.py:10(fib)


# O(2^n) экспоненциальная

# 11/1    0.000    0.000    0.000    0.000 task_3.py:11(fib) 10
# 101/1    0.000    0.000    0.000    0.000 task_3.py:11(fib) 100