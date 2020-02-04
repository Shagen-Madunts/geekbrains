"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
from itertools import count
from sys import argv

start = argv


def generator_1():
    start = int(argv[1])
    for item in count(start=start, step=1):
        if item == 180:
            break
        print(item)


generator_1()
# Пример запуска: python Python\Lesson_4\Task_6\generator_1.py 170

