""""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
filename = "files/task4_output.txt"
spr = {'One': ['Один', 1], 'Two': ['Два', 2], 'Three': ['Три', 3], 'Four': ['Четыре', 4]}

with open('files/task4_source.txt', encoding='utf-8') as file_from:
    for line in file_from:
        value = spr.get(line.split(' —')[0])
        row = f"{value[0]} — {value[1]}"
        with open(filename, 'a', encoding='windows-1251') as file_to:
            file_to.write(f"{row}\n")
