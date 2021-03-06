"""
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков)
 для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f"\n{str(self.matrix[0])}\n{str(self.matrix[1])}"

    def __add__(self, other):
        new_matrix = []
        if len(self.matrix) == len(other.matrix):
            new_matrix = [f for f in self.matrix]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    new_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        else:
            print('\nНе верная размерность матриц!')
        return new_matrix


inst_a = Matrix([[1, 2], [4, 5],[4, 5]])
inst_b = Matrix([[7, 8], [1, 7]])

print(f"Матрица A: {inst_a}\n")
print(f"Матрица B: {inst_b}")
c = inst_a + inst_b
print(f"\nРезультат сложения матриц A и B:")
for el in c:
    print(el)

