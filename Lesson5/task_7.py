# ChainMap - цепочка словарей в виде отдельного списка

from collections import ChainMap

d_1 = {'a': 2, 'b': 4, 'c': 6}
d_2 = {'a': 10, 'b': 20, 'd': 40}

d_map = ChainMap(d_1, d_2)
d_2['a'] = 100
print(d_map)

print(d_map['a'])
print(d_map['d'])

print('*'* 50)
# позволяет взять уже существующую коллекцию и добавить словарь в начало
x = d_map.new_child({'a':111, 'b':222, 'c':333, 'd':444})
print(x)

# обратиться к словарю по индексу
print(d_map.maps[0])
print(d_map.maps[-1])

# узнать какие родители были при создании коллекции методом new_child
print(x.parents)


print('*' * 50)
y = d_map.new_child()
print(y)
print(y['a'])
y['a'] = 1
print(y) # в первом словаре не нашли ключа и поэтому добавили значение в него

# получение ключей и значений

print(list(y))
print(list(y.values()))