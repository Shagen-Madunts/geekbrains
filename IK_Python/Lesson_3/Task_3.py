"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
"""

import random
num_list = list(set([random.randint(1, 100) for _ in range(0, 10)]))
print(f"Исходный массив: {num_list}")
max_el = 0
min_el = 100
for el in num_list:
    if el < min_el:
        min_el = el
    if el > max_el:
        max_el = el

i_max = num_list.index(max_el)
i_min = num_list.index(min_el)
num_list[i_max], num_list[i_min] = num_list[i_min], num_list[i_max]
print(f"Новый массив:    {num_list}\n")
