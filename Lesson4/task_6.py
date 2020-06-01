import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_loop(n):
    if n < 2:
        return n

    first, second = 0, 1
    for i in range(2, n + 1):
        first, second = second, first + second
    return second

# test_fib(fib_loop)

# C:\Users\Admin\Documents\GitHub\gb_ik_python\Lesson4>python -m tim
# eit -n 1000 -s "import task_6" "task_6.fib_loop(500)"
# 1000 loops, best of 5: 140 usec per loop

cProfile.run('fib_loop(500)' )