# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется
# вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * задача считается решённой, если в коде использована функция вычисления хеша (hash(), sha1() или любая другая из
# модуля hashlib)

import hashlib


def count_subs(s: str) -> int:
    assert len(s)> 0 , 'Строка пустая'
    subs = []
    ar_s=[]
    for i in range(len(s)+1):
        for j in range(i+1,len(s)+1):
            if not(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest() in subs) and s[i:j]!=s:
                subs.append(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
                ar_s.append(s[i:j])
    print(ar_s)
    return len(subs)


s=input("Введите строку: ")

count_subs=count_subs(s)

print(f'Количество подстрок {count_subs}')