""""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
import statistics

with open('files/task3_source.txt', encoding='utf8') as f:
    data = f.readlines()
    employees = []
    salary = []
    for i, row in enumerate(data, 1):
        salary.append(int(row.split()[1]))
        if int(row.split()[1]) < 20000:
            employees.append(row.split()[0])
    print(f'Сотрудники: { ", ".join(employees)} имеют оклад менее 20 тыс.'
          f' Средняя величина дохода всех сотрудников: {round(statistics.mean(salary),0)} рублей')
