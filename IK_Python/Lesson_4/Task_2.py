"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""
import cProfile
n_count = 100000


def eratosthenes(m):
    num_list = list(range(n_count + 1))
    num_list[1] = 0
    fin_list = []
    i = 2
    while i <= n_count:
        if num_list[i] != 0:
            fin_list.append(num_list[i])
            for j in range(i, n_count + 1, i):
                num_list[j] = 0
        i += 1
    return fin_list[m] if m < len(fin_list) else "Соответвующее простое число вне полученного списка простых чисел"

"""
cProfile.run('eratosthenes(1000)')
         9597 function calls in 0.045 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.045    0.045 <string>:1(<module>)
        1    0.043    0.043    0.044    0.044 Task_2.py:15(eratosthenes)
        1    0.000    0.000    0.045    0.045 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     9592    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


def define_num(m):
    fin_list = []
    for i in range(2, n_count + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            fin_list.append(i)
    return fin_list[m] if m < len(fin_list) else "Соответвующее простое число вне полученного списка простых чисел"


"""
cProfile.run('define_num(1000)')
         9597 function calls in 31.491 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001   31.491   31.491 <string>:1(<module>)
        1   31.487   31.487   31.490   31.490 Task_2.py:29(define_num)
        1    0.000    0.000   31.491   31.491 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     9592    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
