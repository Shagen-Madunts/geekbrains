"""
На улице встретились count_nodes друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""


def hands(n):
    graph = {}
    for i in range(1, n + 1):
        graph.update({
            i: {x for x in range(1, n + 1) if x != i}
        })
    print(f"Граф рукопожатий {N} друзей: {graph}")

    count = 0
    keys = []
    for i, v in graph.items():
        keys.append(i)
        if i in keys:
            graph.update({
                i: {x for x in range(1, n + 1) if x not in keys}
            })
    for i, v in graph.items():
        count += len(v)
    return count


N = int(input(f"Укажите количество друзей: "))
print(f"Количество рукопожатий {N} друзей: {hands(N)}")
