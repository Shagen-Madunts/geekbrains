"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться
"""

import random

num_list = list(set([random.randint(-20, 20) for _ in range(0, 10)]))
print(f"Массив: {num_list}")
number_list = num_list
for i in range(len(number_list)-1):
    for j in range(len(number_list)-i-1):
        if number_list[j] > number_list[j+1]:
            number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
print(f"перый наименьший: {number_list[0]}, второй: {number_list[1]}")
