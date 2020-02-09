"""
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, с
оответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
"""

source_list = [1, 2, 3, 4, 4, 3, 2, 1, 5]
print(f'Исходный лист {source_list}')
new_list = [i for i in source_list if source_list.count(i) == 1]
print(f'Новый лист {new_list}')