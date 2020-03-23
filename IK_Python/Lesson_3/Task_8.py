"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

source_matrix = [[0 for _ in range(5)] for _ in range(4)]
for i, line in enumerate(source_matrix):
    sum_line = 0
    for j, el in enumerate(line):
        if j == 4:
            source_matrix[i][j] = sum_line
        elif j < len(line):
            source_matrix[i][j] = int(input(f"Введите элемент {i,j}: "))
            sum_line += source_matrix[i][j]
    print()

for k in source_matrix:
    for d in k:
        print(f"{d:>4}", end="")
    print()
