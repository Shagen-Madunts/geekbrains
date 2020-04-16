"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* задача считается решённой, если в коде использована функция вычисления хеша
(hash(), sha1() или любая другая из модуля hashlib)
"""

import hashlib

s = input(f'Введите строку: ')


def calc_count_subs(obj_str):
    def get_subs(obj, list_subs):
        global j
        if len(obj) < 1:
            return
        for j in range(len(obj)):
            list_subs.append(obj[0: j + 1])
            if obj[0: j + 1] == obj:
                list_subs.remove(obj)
        return get_subs(obj[1: j + 1], list_subs)

    fin_list = []
    get_subs(obj_str, fin_list)
    print(f'Список подстрок введенной строки: {fin_list}')

    def search(text: str, subs: str):
        assert len(text) > 0 and len(subs) > 0, 'Не должно быть пустых строк и подстрок'
        assert len(text) >= len(subs), 'Подстрока должна быть короче строки'
        h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()
        len_subs = len(subs)

        for i in range(len(s) - len_subs + 1):
            if h_subs == hashlib.sha1(text[i:i + len_subs].encode('utf-8')).hexdigest():
                if text[i:i + len_subs] == subs:
                    return i
        return -1

    asd = []
    for i in fin_list:
        asd.append(search(obj_str, i))

    print(f'Количество различных подстрок {len(asd)}')


calc_count_subs(s)
