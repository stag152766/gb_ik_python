from collections import defaultdict

a = defaultdict()
print(a)

# подсчет количества повторяющихся символов
s = 'dsfgdsfdtggsfhgdjhgdjhfnkgngnghnfhngddfg'
b = defaultdict(int)
for i in s:
    b[i] += 1
    # если ключа нет, то срабатывает функция int которая генерирует 0
print(b)

# обобщение данных от разных датчиков
list_1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1)]
c = defaultdict(list)
for k, v in list_1:
    c[k].append(v)
print(c)

# когда нужно оставить только уникальные сигналы от каждого датчика
list_2 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 0), ('dog', 1)]
d = defaultdict(set)
for k, v in list_2:
    d[k].add(v)
print(d)

f = defaultdict(lambda: 'unknown')
f.update(rex='dog', tomas='cat')
print(f)
print(f['rex'])
print(f['jerry'])
