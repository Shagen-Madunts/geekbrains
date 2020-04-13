"""
Доработать алгоритм Дейкстры, чтобы он дополнительно возвращал список вершин, которые необходимо обойти
"""

print('Граф в виде списка словарей смежности вершин:')
graph = {
    0: {2: 1, 4: 9, 3: 1},
    1: {3: 4, 2: 9, 6: 7},
    2: {4: 3, 6: 6, 1: 9},
    3: {},
    4: {6: 1},
    5: {6: 5},
    6: {2: 7, 4: 8, 5: 1},
    7: {5: 1, 6: 2}
}

count_nodes = len(graph)

for i in graph:
    print(i, ':', graph[i])


def dijkstra(start, ver_cost, vertexes, min_dist_vertexes, end):
    global first_nb_cost, next_nb
    for neighbor in graph[start]:
        neighbor_cost = ver_cost[start] + graph[start][neighbor]  # стоимость соседа (neighbor_cost) =
        # стоимость начальной вершины (ver_cost[start]) + значение стоимости(ребра) до соседа)
        if not neighbor in ver_cost:  # если соседа (neighbor) нет в словаре (ver_cost)
            ver_cost[neighbor] = neighbor_cost  # записываем стоимость соседа (neighbor_cost)
            min_dist_vertexes[neighbor] = start  # как только стоимость пересчитается запомним предыдущую вершину
        elif not neighbor in vertexes:  # иначе если (neighbor) не в (vertexes)
            if ver_cost[neighbor] > neighbor_cost:  # если старая стомость соседа больше новой стоимости
                ver_cost[neighbor] = neighbor_cost  # тогда записываемему новую стоимость
                min_dist_vertexes[neighbor] = start  # запоминаем (следующая вершина: предыдущая вершина)

    vertexes.append(start)  # добавили рассмотренную вершину в список посещенных

    if count_nodes <= len(vertexes):  # условие выхода из функции
        print('\nИтоговые стоимости для вершин: ', ver_cost)

        path = []  # задаем список вершин для сохранения кратчайшего пути
        path.insert(0, end)  # вставляем конечную вершину в список (path) по индексу (0)

        while True:
            if min_dist_vertexes[end] == -1:  # значение ключа (-1) имеет начальная вершина
                # вот её и ищем в словаре (min_dist_vertexes)
                print(f'Кратчайший путь от заданной начальной в конечную вершину: {path}')
                if path[0] == aim:
                    print('Невозможно построить маршрут!')
                break  # выходим из цикла
            end = min_dist_vertexes[end]  # теперь последней вершиной будет предыдущая
            path.insert(0, end)  # вставляем (е) в список (path) по индексу (0)

        return path

    for d in ver_cost:  # примем первого соседа, которого не рассматривали с его стоимостью как первую следующую по пути
        if d not in vertexes:
            first_nb_cost = ver_cost[d]
            next_nb = d
            break

    for y in ver_cost:  # для каждой вершины
        if ver_cost[y] < first_nb_cost and not y in vertexes:  # если стоимость вершины < стоимости первой попавшейся
            # вершины и ее еще не рассматривали
            first_nb_cost = ver_cost[y]  # стоимость первой вершины перезаписываем
            next_nb = y

    start = next_nb  # теперь текущей вершиной start будет вершина d

    dijkstra(start, ver_cost, vertexes, min_dist_vertexes, end)  # вызовем рекурсивно нашу функцию,
    # но уже с новой стартовой точкой


def get_variables(s, f):
    global aim
    aim = f
    nodes = []  # список вершин, которые посетили
    dict_cost = {i: float('inf') for i in range(count_nodes)}  # словарь {вершина : стоимость}
    dict_dist = {i: -1 for i in range(count_nodes)}  # словарь для сохранения пути до вершины
    go = s  # стартовая вершина (откуда)
    stop = f  # конечная вершина (куда)
    dict_cost[go] = 0  # задаем значение стоимости для стартовой вершины
    return dijkstra(go, dict_cost, nodes, dict_dist, stop)


out = int(input(f"\nУкажите номер стартовой вершины: "))
to = int(input(f"Укажите номер конечной вершины: "))
get_variables(out, to)
