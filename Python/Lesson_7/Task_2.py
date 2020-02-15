"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def calc_consumption(self):
        pass


class Clothes(AbstractClass):
    def __init__(self, name, size):
        self.name = name
        self.param = size

    @property
    def calc_consumption(self):
        if self.name == 'Пальто':
            return round(self.param / 6.5 + 0.5, 1)
        elif self.name == 'Костюм':
            return round(2 * self.param + 0.3, 1)
        else:
            return 0


class Calc(Clothes):
    def __str__(self):
        if self.calc_consumption == 0:
            return f"Не подходящий тип одежды. Укажите 'Пальто' или 'Костюм'"
        return f"Расход ткани на {self.name}: {self.calc_consumption}"

    def __add__(self, other):
        return self.calc_consumption + other.calc_consumption


inst_a = Calc('Костюм', 180)
print(inst_a)

inst_b = Calc('Пальто', 54)
print(inst_b)

print(f"Общий расход ткани: {inst_a + inst_b}")
