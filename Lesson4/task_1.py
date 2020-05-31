import timeit

x = 2 + 2

print(timeit.timeit('x = 2 + 2'))
print(timeit.timeit('x = sum(range(10))'))

# \Lesson4>python -m timeit -n 100 -s "import les_4_task_1"