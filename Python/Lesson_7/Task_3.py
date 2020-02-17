"""Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не
целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого
числа. Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных
двух клеток. Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
двух клеток больше нуля, иначе выводить соответствующее сообщение. Умножение. Создается общая клетка из двух. Число
ячеек общей клетки определяется как произведение количества ячеек этих двух клеток. Деление. Создается общая клетка
из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток. В классе
необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам. Метод должен возвращать строку вида **\n\n***..., где количество ячеек между
\n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все
оставшиеся. Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: **\n\n. Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: **\n\n***. """


class Cell:
    def __init__(self, number):
        self.cell = ""
        self.number = number

    def __add__(self, other):
        return self.number + other

    def __sub__(self, other):
        if self.number - other > 0:
            return self.number - other
        else:
            print('Разница меньше нуля или ее нет')

    def __mul__(self, other):
        return self.number * other

    def __truediv__(self, other):
        return self.number // other

    def make_order(self, cells_in_row):
        while self.number > 0:
            self.number -= cells_in_row
            if self.number < 0:
                self.cell += ("*" * (cells_in_row + self.number) + "\n")
            else:
                self.cell += ("*" * cells_in_row + "\n")
        return self.cell

    def __call__(self, param_2):
        self.number = param_2


inst = Cell(42)
print(inst + 15)
print(inst * 15)
print(inst - 15)
print(inst / 15)
print(inst.make_order(20))

