"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть); проанализировать 3 варианта и выбрать оптимальный;

c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.

ЗАДАЧА: В одномерном массиве целых чисел определить два наименьших элемента.
"""

from sys import getsizeof
from collections import Mapping, Container
from numpy import unicode
from random import randint


"""
3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] win32
Размер Вариант 1: 28 байт
Размер Вариант 2: 156 байт
Размер Вариант 3: 140 байт
ВЫВОД: Вариант 1 ч точки зрения использования памаяти предпочтительнее (28 байт в сравнении с 156 и 140). 
Но с точки зрения скорости выполнения гораздо менее эффективен. Поэтому нужно выбирать тот или иной варинат
кода после понимания размера исходного массива целых чисел. 
"""
nums_list = [randint(1, 1000) for _ in range(1000)]
numbers = nums_list


def size_objects(obj, seen):
    d = size_objects
    if id(obj) in seen:
        return 0

    size_o = getsizeof(obj)
    seen.add(id(obj))

    if isinstance(obj, str) or isinstance(0, unicode):
        return size_o

    if isinstance(obj, Mapping):
        return size_o + sum(d(k, seen) + d(v, seen) for k, v in obj.iteritems())

    if isinstance(obj, Container):
        return size_o + sum(d(x, seen) for x in obj)

    return size_o

# Вариант 1
nums = numbers
for i in range(len(nums) - 1):
    for j in range(len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(f"Размер Вариант 1: {size_objects(nums[0],set())} байт")

# Вариант 2
s = numbers
numMin1 = numMin2 = s[0]
iMin1 = iMin2 = 0
for i, item in enumerate(s):
    if numMin1 >= item and iMin1 != i:
        numMin2 = numMin1
        numMin1 = item
        iMin1 = i
    elif numMin2 >= item and iMin2 != i:
        numMin2 = item
        iMin2 = i
print(f"Размер Вариант 2: {size_objects([numMin1, numMin2, iMin1, iMin2, s[0]],set())} байт")

# Вариант 3
nums = numbers
if nums[0] > nums[1]:
    min_idx_1 = 0
    min_idx_2 = 1
else:
    min_idx_1 = 1
    min_idx_2 = 0
for j in range(2, 100):
    if nums[j] < nums[min_idx_1]:
        spam = min_idx_1
        min_idx_1 = j
        if nums[spam] < nums[min_idx_2]:
            min_idx_2 = spam

    elif nums[j] < nums[min_idx_2]:
        min_idx_2 = j
print(f"Размер Вариант 3: {size_objects([min_idx_1, min_idx_2, nums[0]],set())} байт")
