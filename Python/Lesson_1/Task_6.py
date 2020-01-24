"""
 Спортсмен занимается ежедневными пробежками.
 В первый день его результат составил a километров.
 Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
 Требуется определить номер дня, на который общий результат спортсмена составит не менее b километров.
 Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

a = int(input('Введите результат первого дня: '))
b = int(input('Введите цель спортсмена: '))
if a >= b:
    print('Цель должна быть больше результатов первого дня')
elif a <= 0 or b <= 0:
    print('Введенные значения должны быть натуральными')
else:
    i = 1
    while a < b * 1.1:
        print(f'{i}-й день: {a:.2f}')
        i += 1
        a = a * 1.1
    print(f'\nОтвет: на {i-1}-й день спортсмен достиг результата — не менее {b} км.')
