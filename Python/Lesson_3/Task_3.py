def my_func(arg1, arg2, arg3):
    """
    Реализовать функцию my_func(), которая принимает три позиционных аргумента,
    и возвращает сумму наибольших двух аргументов
    :param arg1: Значение 1
    :param arg2: Значение 1
    :param arg3: Значение 1
    :return: сумма двух наибольших
    """
    sum_arg = 0
    try:
        minimum = min(arg1, arg2, arg3)
        if arg1 == minimum:
            sum_arg = arg2 + arg3
        elif arg2 == minimum:
            sum_arg = arg1 + arg3
        else:
            sum_arg = arg1 + arg2
    except Exception as e:
        print(f'Введенные значения не числа. Ошибка: {e}')
    return sum_arg


print(f'Результат сумирования: {my_func(1, 12, 3)}')
