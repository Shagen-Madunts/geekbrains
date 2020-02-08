""""
Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import statistics
import json

filename = f'files/task7_source.txt'
profit = []
report = []
records = {}
with open(filename, encoding='utf-8') as file:
    for line in file:
        data = line.split()
        profit.append(int(data[2]) - int(data[3]))
        avg_profit = [el for el in profit if el > 0]
        record = {data[0]: int(data[2]) - int(data[3])}
        records.update(record)
        print(f'Прибыль {data[0]} : {int(data[2]) - int(data[3])}')
    record_profit = {'average_profit': statistics.mean(profit)}
    report.append(records)
    report.append(record_profit)
    print(f'Средняя прибыль фирм: {round(statistics.mean(avg_profit),0)}')
    print(report)

filename_out = f'files/task7_output.json'
with open(filename_out, 'w', encoding='utf8') as j:
    json.dump(report,j, allow_nan=True, ensure_ascii=False, indent=4, default=str)


