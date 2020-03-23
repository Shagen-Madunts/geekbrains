"""
Определить, какое число в массиве встречается чаще всего.
"""

import random
num_list = [random.randint(1, 10) for _ in range(0, 20)]
print(f"Массив: {num_list}")
el_dict = {}
for el in set(num_list):
    r_l = []
    i = 0
    while i < len(num_list):
        if num_list[i] == el:
            r_l.append(el)
        i += 1
    el_dict.update({
        el: len(r_l)
    })
max_value = 1
key = ''
for k, val in el_dict.items():
    if val > max_value:
        max_value = val
        key = k

print(f"Число {key} встречается {max_value} раз(-а)")
