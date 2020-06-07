# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

k = int(input('Введите количество предпиятий: '))
enterprises = []

New_Enterprise = namedtuple('New_Enterprise', 'name, quarters, profit')

for i in range(1, k + 1):
    name = input('Введите название предприятия: ')
    quarters = [float(input('Квартал 1: ')), float(input('Квартал 2: ')),
                float(input('Квартал 3: ')), float(input('Квартал 4: '))]
    profit = sum(quarters) / len(quarters)
    enterprise = New_Enterprise(name, quarters, profit)
    enterprises.append(enterprise)

print(enterprises)
sum = 0
for item in enterprises:
    sum += item.profit
avg = sum / k
print(f'Средняя прибыль за год для всех предприятий: {avg}')

for item in enterprises:
    if avg < item.profit:
        print(f'Прибыль выше среднего: {item.name} ')
    else:
        print(f'Прибыль ниже среднего: {item.name}')
