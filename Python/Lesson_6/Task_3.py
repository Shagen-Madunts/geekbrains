"""
Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 14000, "bonus": 5000}


class Position(Worker):
    def get_full_name(self):
        print(f"Имя: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Доход: {int(self._income['wage']) + int(self._income['bonus'])}")


inst = Position("Ivan", "Petrov", "CEO")
print(inst.name, inst.surname, inst.position)
inst.get_full_name()
inst.get_total_income()
