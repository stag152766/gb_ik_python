import random


a = [random.randint(-100,100) for _ in range(100)]
print(a)

arr_below = []
arr_large = []

for i in a:
    if i < 0:
        arr_below.append(i)
    else:
        arr_large.append(i)

print(arr_below)
print(arr_large)


