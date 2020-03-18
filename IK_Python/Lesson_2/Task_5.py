"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
"""

start = 32
stop = 128
count = len(range(start, stop))
while count > 0:
    if count // 10 == 0:
        stop = count
    else:
        stop = 10
    for i in range(start, start + stop):
        print(f"{i}-{chr(i)}", end=" ")
    print('\n')
    start += 10
    count -= 10
