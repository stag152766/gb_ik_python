import random

from collections import deque

a = deque()
b = deque('asffgfg')
c = deque([1, 2, 3, 4, 5])
print(a, b, c, sep='\n')

# О(1) const
# O(n)

# в очереди остались последнии элементы в количестве, которое мы указали
b = deque('abcdef', maxlen=3)
c = deque([1, 2, 3, 4, 5], maxlen=4)
print(b, c, sep='\n')

# самое последнее в очередях - добавление элемента в начало или конец

print('*' * 50)
d = deque([i for i in range(5)], maxlen=7)
d.append(5)
d.appendleft(6)
print(d)
d.extend([7, 8, 9])
d.extendleft([10, 11, 12])
print(d)

print('*' * 50)
f = deque([i for i in range(5)], maxlen=7)
print(f)
x = f.pop()
y = f.popleft()
print(f, x, y, sep='\n')

print('*' * 50)
g = deque([i for i in range(5)], maxlen=7)
print(g.count(2))
print(g.index(3))
g.insert(2, 6)
print(g)


g.reverse()
print(g)

g.rotate(3)
print(g)


a = [random.randint(-100,100) for _ in range(10)]
print(a)

# arr_below = []
# arr_large = []

deq = deque()

for i in a:
    if i > 0:
        deq.append(i)
    else:
        deq.appendleft(i)
print(deq)

print('*' * 50)

with open('log.txt', 'r', encoding='utf-8') as f:
    last_ten = deque(f, 10)
print(last_ten)