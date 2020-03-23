"""
В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше
введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ.
"""

import random

user_try = 1
auto_rand = random.randint(0, 100)
print('Угадайте случайное число. У вас 10 попыток.')
print(auto_rand)
while user_try <= 10:
    user_num = int(input('Введите загаданное число: '))
    if user_num == auto_rand:
        print('\nПоздравляем! Вы отгадали!')
        break
    elif user_num > auto_rand:
        print('Ваше число больше загаданного')
    else:
        print('Ваше число меньше загаданного')
    left = 10 - user_try
    print(f'Осталось попыток: {left}')
    user_try += 1
    if user_try == 10:
        print('\nУ вас не осталось попыток!')
        break