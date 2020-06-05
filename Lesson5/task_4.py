from collections import OrderedDict

a = {'cat': 5, 'mouse': 4, 'dog': 2}
# отсортировать ключ - значение и в качестве ключа х нулевое
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
print(new_a)

# отсортировать по значению
new_b = OrderedDict(sorted(a.items(), key=lambda x: x[1]))
print(new_b)

# при сравнении OrderedDict важен порядок элементов
print(new_a == new_b)

c = {('frog', 2), ('hourse', 3)}
f = {('hourse', 3), ('frog', 2)}
print(c == f)

new_b.move_to_end('mouse', last=False)
print(new_b)

new_b.popitem(last=False)
print(new_b)

# новый элемент всегда добавляется в конец
new_b['cow'] = 1
print(new_b)

# значение изменилось, а порядок остался прежним
new_b['dog'] = 8
print(new_b)

print('*' * 50)
# сортировка по длине ключа
new_c = OrderedDict(sorted(a.items(), key = lambda x: len(x[0])))
print(new_c)

# переворачивание
for key in reversed(new_c):
    print(key, new_c[key])
# обычный словарь не подойдет, так как объекты в нем не отсортированы

