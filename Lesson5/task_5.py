from collections import deque, OrderedDict, defaultdict

# В log файл сервер добавляет ip-адреса, с которых пришёл запрос.
# Проанализировать последние N адресов и сохранить в новый
# файл пары значений “ip-адрес - количество запросов”.
#  Исключить локальные ip-адреса: 192.168.*.*
#  Сохранить исходный порядок адресов.

N = 3000
with open('big_log.txt', 'r', encoding='utf-8') as f:
    log = deque(f, maxlen=N)
print(log)

data = OrderedDict()
spam = defaultdict(int)

for item in log:
    ip = item[:-1]

    if not ip.startswith('192.168'):
        spam[ip] += 1  # считает количество по конкретному ip
        data[ip] = 1  # сохраняет порядок
print(spam)
print(data)

# в словарь data добавляем ключи из словаря spam
# ведь при изменении значения позиция в словаре OD не меняется
data.update(spam)
print(data)

with open('data.txt', 'w', encoding='utf-8') as f:
    for k, v in data.items():
        f.write(f'{k} - {v}\n')
