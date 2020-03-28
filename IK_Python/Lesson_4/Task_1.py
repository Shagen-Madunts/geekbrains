"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.

ЗАДАЧА: В одномерном массиве целых чисел определить два наименьших элемента.
"""

import cProfile
import random

SIZE = 10000
num_list = [random.randint(-9000, 9000) for _ in range(SIZE)]

# Вариант 1
def version_1(s):
    number_list = s
    for i in range(len(number_list) - 1):
        for j in range(len(number_list) - i - 1):
            if number_list[j] > number_list[j + 1]:
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
    return number_list[0], number_list[1]

"""

python -m timeit -n 1000 -s "import Task_1" "Task_1.version_1"
1000 loops, best of 5: 28.7 nsec per loop


cProfile.run('version_1(num_list)')
         10004 function calls in 10.488 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   10.488   10.488 <string>:1(<module>)
        1   10.486   10.486   10.488   10.488 Task_1.py:19(version_1)
        1    0.000    0.000   10.488   10.488 {built-in method builtins.exec}
    10000    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# Вариант 2
def version_2(s):
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
    return iMin1, iMin2

"""
python -m timeit -n 1000 -s "import Task_1" "Task_1.version_2"
1000 loops, best of 5: 28.6 nsec per loop

cProfile.run('version_2(num_list)')
         4 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 Task_1.py:43(version_2)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


# Вариант 2
def version_3(s):
    if s[0] > s[1]:
        min_idx_1 = 0
        min_idx_2 = 1
    else:
        min_idx_1 = 1
        min_idx_2 = 0
    for j in range(2, SIZE):
        if s[j] < s[min_idx_1]:
            spam = min_idx_1
            min_idx_1 = j
            if s[spam] < s[min_idx_2]:
                min_idx_2 = spam

        elif s[j] < s[min_idx_2]:
            min_idx_2 = j
    return s[min_idx_1], s[min_idx_2]

"""

python -m timeit -n 1000 -s "import Task_1" "Task_1.version_3"
1000 loops, best of 5: 28.6 nsec per loop


cProfile.run('version_3(num_list)')
         4 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 Task_1.py:71(version_3)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# Вывод: Наиболее эффективно на имеющемся объеме выборки использовать 2 или 3 вариант решения задачи, поскольку
# в сравнении с 1 вариантом решения оба значительно меньше затраичивают ресурсов как по времени, так и по
# количеству запусков функции тем самым являются более эффективными.
