""""
 Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке.
"""


with open('files/task2_source.txt', encoding='utf8') as f:
    data = f.readlines()
    print(f'Количество строк: {len(data)}\n')
    for i, row in enumerate(data, 1):
        print(f'Количество слов в {i} строке: {len(set(row.split()))}')
