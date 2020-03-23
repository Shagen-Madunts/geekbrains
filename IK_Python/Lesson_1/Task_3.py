"""
Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

from random import randint
from random import uniform
from random import random

a = int(input(f'Введите нижнюю границу диапазона целых чисел: '))
b = int(input(f'Введите вверхнюю границу диапазона целых чисел: '))
print(f'Случайное целое число в диапазоне от {a} до {b}: {randint(a,b)}\n')

a = float(input(f'Введите нижнюю границу диапазона вещественных чисел: '))
b = float(input(f'Введите вверхнюю границу диапазона вещественных чисел: '))
print(f'Случайное целое число в диапазоне от {a} до {b}: {uniform(a,b)}\n')

a = ord(input(f'Введите нижнюю границу диапазона символов: '))
b = ord(input(f'Введите вверхнюю границу диапазона символов: '))
print(f'Случайное целое число в диапазоне от {chr(a)} до {chr(b)}: {chr(int(random() * (b - a + 1)) + a)}\n')