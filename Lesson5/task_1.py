from collections import Counter

a = Counter()
b = Counter('abracadabra')
c = Counter({'red': 2, 'blue': 3})
d = Counter(cats=3, dogs=5)

print(a, b, c, d, sep='\n')

print(b['z'])
b['z'] = 0
print(b)

# возвращает набор итерируемых объектов, у которых значение > 0
print(list(b.elements()))

# возвращает список кортежей (ключ - значение) + фильтрация по убыванию
print(b.most_common(2))

g = Counter(a=4, c=-2, d=0)
f = Counter(a=1, c=3, d=-2)
g.subtract(f)
print(g)

print('*' * 50)
print(set(g))
print(dict(g))
g.clear()
print(g)

x = Counter(a=3, b=2)
y = Counter(a=1, b=1)

print(x + y)
print(x - y)  # выводим только положительные
print(x & y)
print(x | y)

print('*' * 50)
z = Counter(a=2, b=-4)
print(+z)  # выводит только положительные
print(-z)  # меняет знак и выводит только положительные
