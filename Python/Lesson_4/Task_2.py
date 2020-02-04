"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""
from random import random

source_list = [round(x * random(), 1) for x in range(10)]
print(f'Исходный лист {source_list}')
new_list = [source_list[i] for i in range(len(source_list)) if source_list[i] > source_list[i-1]]
print(f'Новый лист {new_list}')
