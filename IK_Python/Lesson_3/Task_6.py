"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать
"""

import random

num_list = list(set([random.randint(-20, 20) for _ in range(0, 20)]))
print(f"Массив: {num_list}")
maximum, ind_max = 0, 0
minimum, ind_min = 0, 0
for i, el in enumerate(num_list):
    if el > maximum:
        maximum = el
        ind_max = i
    if el < minimum:
        minimum = el
        ind_min = i
el_sum = 0
if ind_max - ind_min > 2:
    for i in num_list[ind_min + 1: ind_max]:
        el_sum += i
elif ind_min - ind_max > 2:
    for i in num_list[ind_max + 1:ind_min]:
        el_sum += i
else:
    el_sum = 0
print(f"Сумма между элементами {minimum} и {maximum} равна: {el_sum}")
