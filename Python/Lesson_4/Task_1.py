"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, hours, base_in_hour, prize = argv


def wage():
    hours = int(argv[1])
    base_in_hour = int(argv[2])
    prize = int(argv[3])
    try:
        print(f'Размер заработной платы: {hours * base_in_hour + prize} рублей')
    except Exception as e:
        print(f'Ошибка {e}')


wage()

# Пример запуска: python Python\Lesson_4\Lesson_2.py 168 200 15000
