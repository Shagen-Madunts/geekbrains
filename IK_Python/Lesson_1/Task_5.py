"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

first, last = ord('a'), ord('z')
pos = int(input(f'Введите число в диапазоне от {first} до {last}: '))
print(f'Это буква: {chr(pos)}')
