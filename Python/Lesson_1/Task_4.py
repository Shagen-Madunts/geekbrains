"""
 Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
 Для решения используйте цикл while и арифметические операции.
"""


number = int(input('Введите число: '))
if 10 <= number >= -10:
    var = number // 10
    max_numeral = number % 10
    while var > 0:
        if var % 10 > max_numeral:
            max_numeral = var % 10
        var = var // 10
    print(f'Наибольшая цифра {max_numeral}')
    print('end program')
else:
    print('Введите число а не цифру!')
    print('end program')
