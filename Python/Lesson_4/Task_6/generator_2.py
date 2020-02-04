"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
from itertools import cycle

source = [1, 2]


def generator_2():
    for item in cycle(source):
        print(item)


generator_2()
# Пример запуска: python Python\Lesson_4\Task_6\generator_2.py
