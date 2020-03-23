"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
"""

x1 = float(input(f"Введите координату x первой точки: "))
y1 = float(input(f"Введите координату y первой точки: "))
x2 = float(input(f"Введите координату x второй точки: "))
y2 = float(input(f"Введите координату y второй точки: "))

if x2 - x1 != 0:
    print(f"\nУравнение прямой, проходящей через точки "
          f"{x1,y1} и {x2, y2}: y = {(y2-y1)/(x2-x1)}*x + {y2 - (y2-y1)/(x2-x1)*x2}")
elif y2 - y1 != 0:
    print(f"\nУравнение прямой, проходящей через точки {x1,y1} и {x2, y2}: x = {x1}")
else:
    print("Уравнение составить нельзя")