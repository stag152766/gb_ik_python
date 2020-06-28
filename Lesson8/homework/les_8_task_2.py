# Доработать алгоритм Дейкстры, чтобы он дополнительно
# возвращал список вершин, которые необходимо обойти.
from collections import deque

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
    min_cost = 0
    vertex_d = {}
    vertex_d[start] = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
                vertex_d[start] = parent[i]

    # print(vertex_d)
    new_dict = {}

    def way(dict, n):
        start = 0
        if dict[n] != start:
            new_list.appendleft(dict[n])
            way(dict, dict[n])
        else:
            new_list.appendleft(dict[n])
            if i != 0:
                new_list.append(i)
        return new_list

    for i in range(len(vertex_d)):
        new_list = deque()

        new_dict[i] = list(way(vertex_d, i))

    #print(new_dict)
    for k, v in new_dict.items():
        print(f'Для вершины {k} путь: {v}')

    return cost


s = int(input('От какой вершины идти: '))
print(dijkstra(g, s))
