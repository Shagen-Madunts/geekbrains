""""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
"""


filename = f'files/task5_output.txt'
numbers = [1, 20, 3, 40]

with open(filename, 'w') as f:
    for i in numbers:
        f.writelines(f"{i} ")

with open(filename) as file:
    data = file.readline().split()
    print(f'Cумма чисел в файле: {sum([int(x) for x in data])}')
