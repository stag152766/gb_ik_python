import sys

print(sys.version, sys.platform)

a = 5
b = 125.54
c = 'Hello World!'

print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))

lst = [i for i in range(10)]
print(sys.getsizeof(lst))

def show_size(x, level = 0):
    print('\t' * level, f'type={x.__class__}, size={sys.getsizeof(x)}, object={x}')

    # деление составных объектов на части

    # проверка является ли объект итетируемым
    if hasattr(x, '__iter__'):
        # проверка является ли объект словарем
        if hasattr(x, 'items'):
            # берем каждое значение словаря и передаем в рекурсивную функцию
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)

show_size(a)
show_size(b)
show_size(c)
show_size(lst)

print('*' * 50)
t = tuple(lst) # поиск элемента в кортеже или списке зависит от размера
show_size(t)

print('*' * 50)
s = set(lst) # поиск элемента во множестве занимает константное время
show_size(s)

print('*' * 50)
d = {str(i): i for i in range(10)}
show_size(d)
