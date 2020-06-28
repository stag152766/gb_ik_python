dict = {0: 0, 2: 0, 1: 2, 3: 0, 4: 2, 6: 4, 5: 6}


def way(dict, n):
    start = 0
    if dict[n] != start:
        print(dict[n])
        way(dict, dict[n])
    else:
        print(dict[n])

for i in range(len(dict)):
    print(f'Вершина {i}')
    way(dict, i)


