"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

num = int(input(f'Введите число: '))
count_even = 0
count_not_even = 0
while num > 0:
    if num % 2 == 0:
        count_even += 1
    else:
        count_not_even += 1
    num = num // 10
print(f"Количество четных чисел: {count_even}, нечетных {count_not_even}")
