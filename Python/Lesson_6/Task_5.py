"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self):
        self.title = 'Parker'

    def drow(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self):
        super().__init__()

    def drow(self):
        print(f"Отрисовка ручки {self.title}")


class Pencil(Stationery):
    def __init__(self):
        super().__init__()

    def drow(self):
        print(f"Отрисовка карандаша {self.title}.")


class Handle(Stationery):
    def __init__(self):
        super().__init__()

    def drow(self):
        print(f"Отрисовка новой ручки {self.title}.")


a = Stationery()
a.drow()
b = Pen()
b.drow()
c = Pencil()
c.drow()
d = Handle()
d.drow()
