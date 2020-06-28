from collections import namedtuple

# 1. списки смежности

graph = []

graph.append([1, 2])
graph.append([0, 2, 3])
graph.append([0, 1])
graph.append([1])

print(graph)
print(*graph, sep='\n')
# как проверить что из вершины 1 мы попадем в вершину 3?
# - перебрать весь список

print('*' * 50)

# 2. ориентированный граф
graph_2 = {
    0: {1, 2},
    1: {0, 2, 3},
    2: {0, 1},
    3: {1}
}
print(graph_2)

# как проверить что из вершины 1 мы попадем в вершину 3?
if 3 in graph_2[1]:
    print(True)

# 3. взвешенный граф
print('*' * 50)
Vertex = namedtuple('Vertex', ['vertex', 'edge'])
graph_3 = []

graph_3.append([Vertex(1, 2), Vertex(2, 3)])
graph_3.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
graph_3.append([Vertex(0, 3), Vertex(1, 2)])
graph_3.append([Vertex(1, 1)])

print(*graph_3, sep='\n')

# как проверить что из вершины 1 мы попадем в вершину 3?
for v in graph_3[1]:
    if v.vertex ==3:
        print(True)

class Graph:
    def __init__(self, vertex, edge,spam):
        self.vertex = vertex
        self.edge = edge
        self.spam = spam

