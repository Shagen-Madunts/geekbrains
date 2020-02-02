"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""
user_data = 0
result = 0
while user_data != 'stop':
    user_data = input('Введите несколько чисел через пробел и нажмите Enter: ')
    if user_data == 'stop':
        break
    else:
        user_data = list(user_data.split(' '))
        index_stop = None
        if 'stop' in user_data:
            index_stop = user_data.index('stop')
            user_data.pop(index_stop)
            user_data = list(map(float, user_data[:index_stop]))
            result = result + sum(user_data)
            print(result)
            break
        else:
            user_data = list(map(float, user_data[:index_stop]))
            result = result + sum(user_data)
            print(result)
print('end program\n ')
