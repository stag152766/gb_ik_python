# На улице встретились N друзей. Каждый пожал руку всем
# остальным друзьям (по одному разу).
# Сколько рукопожатий было?

n = int(input('Введите количетсво друзей: '))


def create_graph(n):
    graph = [[1 for _ in range(n)] for _ in range(n)]
    for i in range(len(graph)):
        graph[i][i] = 0
    print(*graph, sep='\n')
    return graph


def handshakes(n):
    count = 0
    for i in create_graph(n):
        for j in i:
            if j == 1:
                count += 1
    return round(count / 2)


print(f'Количество рукопожатий: {handshakes(n)}')
