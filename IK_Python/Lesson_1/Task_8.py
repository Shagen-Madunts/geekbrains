"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if b < a < c or c < a < b:
    print(f"Среднее значение: {a}")
elif a < b < c or c < b < a:
    print(f"Среднее значение: {b}")
else:
    print(f"Среднее значение: {c}")