"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

n = input('Введите числа через пробел: ')
max_num = 0
f_n = ''
f_s = 0
for i in n.split(" "):
    s = 0
    for j in i:
        s += int(j)
    if s > max_num:
        f_n = i
        f_s = s
        max_num = s
print(f"Число: {f_n}, сумма цифр в числе: {f_s}")