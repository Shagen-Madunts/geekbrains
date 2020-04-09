"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

import random

num_list = list(set([random.randint(0, 49) for _ in range(1, 11)]))
print(f"Массив исходный: {num_list}")

# Разделим массив на 2 части и применим функцию merge
def sep_merge(array):
    if len(array) <= 1:
        return array[:]
    else:
        mid = int(len(array) / 2)
        left = array[:mid]
        right = array[mid:]
    return merge(sep_merge(left), sep_merge(right))


def merge(left, right):
    fin = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            fin.append(left[i])
            i += 1
        else:
            fin.append(right[j])
            j += 1
    fin += left[i:] + right[j:]
    return fin


print(f"Отсортированный: {sep_merge(num_list)}\n")
