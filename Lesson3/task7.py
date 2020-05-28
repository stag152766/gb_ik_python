k = int(input('Введите количество предпиятий: '))

enterprizes = {}

for i in range(1, k+1):
    name = input('Введите название предприятия: ')
    enterprizes[name] = [float(input('План: ')), float(input('Факт: '))]
    enterprizes[name].append(enterprizes[name][1] / enterprizes[name][0])

print('Фактическая прибыль равна больше 10, но план не выполнен (меньше 100%)')

for key, value in enterprizes.items():
    if value[1] > 10 and value[2] < 1:
        print(f'Предприятие {key} заработало {value[1]}, что составило {value[2] * 100: .2f}%')
