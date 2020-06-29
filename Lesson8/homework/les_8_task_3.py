# Написать программу, которая обходит не взвешенный
# ориентированный граф без петель, в котором все вершины
# связаны, по алгоритму поиска в глубину (Depth-First Search).
# граф должен храниться в виде списка смежности;
# генерация графа выполняется в отдельной функции, которая
# принимает на вход число вершин.

def graph(n):
    graph = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i].append(j)

    return graph


n = int(input('Ввидите количество вершин: '))
graph = graph(n)
print(graph)

is_visited = [False] * n
prev = [-1] * n


def dfs(start, graph):
    if not is_visited[start]:
        is_visited[start] = True
        prev[start] = start
        for i in graph[start]:
            dfs(i, graph)
    return prev


result = dfs(0, graph)
print(result)
