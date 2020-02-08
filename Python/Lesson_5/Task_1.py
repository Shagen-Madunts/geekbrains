""""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

filename = 'files/task1_output.txt'
data = ' '
with open(filename, 'w', encoding='utf8') as f:
    while data != '':
        data = input(f'Вводите данные: ')
        f.writelines(f"\n{data}")
