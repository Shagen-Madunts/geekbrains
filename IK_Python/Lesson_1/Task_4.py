"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

a = ord(input(f'Введите первую букву: '))
b = ord(input(f'Введите вторую букву: '))
a_pos = a - ord('a') + 1
b_pos = b - ord('a') + 1
print(f'Позиция первой буквы {a_pos}, второй {b_pos}')
print(f'Между буквами {abs(a-b)-1} букв')


