def dev_numbers(number1, number2):
    """
    Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
    :param number1: любое число
    :param number2: любое число
    :return: результат деления
    """
    while number2 == 0:
        print('Деление на ноль недопустимо!')
        number2 = int(input('Введите другой делитель: '))

    return number1 / number2


num_1 = int(input('Введите делимое: '))
num_2 = int(input('Введите делитель: '))

print(f'Результат деления: {dev_numbers(num_1, num_2)}')
print('end program')
