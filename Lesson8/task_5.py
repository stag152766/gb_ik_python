# поиск кратчайшего пути Декстры
# для взвешенного графа

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0 # показывает двигаемся дальше по графу или нет

    while min_cost < float('inf'):

        is_visited[start] = True

        # пройдемся по той строке, в которой хранится старт
        # номер строки = номер вершины (старт)
        for i, vertex in enumerate(graph[start]):
            # если у вершины есть ребро и вершину не посещали, то проверим расстояние
            if vertex != 0 and not is_visited[i]:

                # если расстояниие
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

                    # обошли все вершины и записали все минимальные расстояния до них

        min_cost = float('inf')

        # пройдем по всем вершинам графа
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    # вернуть список стоимостей путей до каждой вершины
    return cost


s = int(input('От какой вершины идти: '))
print(dijkstra(g, s))
