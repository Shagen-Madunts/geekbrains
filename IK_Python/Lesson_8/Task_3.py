"""
Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин
"""


def gen_graph(n):
    g = {}
    d = 2
    k = 4
    for i in range(1, n):
        g.update({i: [x for x in range(d, k) if x != i]})
        d += 2
        k += 2
    for i in range(int(n/2), n):
        g.update({i: [i + 1]})
    for i in range(n, n + 1):
        g.update({i: []})
    return g


count_vertexes = int(input(f"Укажите количество вершин: "))
graph = gen_graph(count_vertexes)

print('Граф:')
for key, val in graph.items():
    print(key, ":", val)


def dfs(g, node, path=None):
    if path is None:
        path = []
    path += [node]
    for n in g[node]:
        if n not in path:
            path = dfs(g, n, path)
    return path


print(f"Пути от первой вершины графа: {dfs(graph, 1)}")
