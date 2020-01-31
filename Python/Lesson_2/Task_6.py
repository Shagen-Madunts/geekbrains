"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
spr_article = []
dict_info = {}
list_keys = ['Название', 'Цена', 'Количество', 'Ед.']
i = 0
while i != 'stop':
    item = input(f'Нажмите Enter и вводите данные по {i+1} товару или напишите stop: ')
    if item == 'stop':
        print('Собранные данные:\n ')
        break
    list_keys = ['Название', 'Цена', 'Количество', 'Ед.']
    for keys in list_keys:
        values = input(f'Введите значение по полю {keys}: ')
        dict_info[keys] = values
    spr_article.append((i, dict_info))
    i += 1
print(spr_article)
if len(spr_article) > 1:
    analytics_dict = {}
    list_names = []
    list_prices = []
    list_counts = []
    list_eds = []

    for i in spr_article:
        k_name = i[1].get(list_keys[0])
        list_names.append(k_name)

        k_price = i[1].get(list_keys[1])
        list_prices.append(k_price)

        k_count = i[1].get(list_keys[2])
        list_counts.append(k_count)

        k_ed = i[1].get(list_keys[3])
        list_eds.append(k_ed)

    analytics_dict.update({
        list_keys[0]: list_names,
        list_keys[1]: list_prices,
        list_keys[2]: list_counts,
        list_keys[3]: list_eds
    })
    print(f'Аналитика о товарах:\n {analytics_dict}')
    print('end program')

else:
    print('end program')

