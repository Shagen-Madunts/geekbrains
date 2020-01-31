"""
Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
list_input = []
i = 0
while i != 'stop':
    item = input(f'Введите {i} значение для заполнения списка: ')
    list_input.append(item)
    i += 1
    if item == 'stop':
        list_input.remove('stop')
        break
print(list_input)

if len(list_input) % 2 == 0:
    new_list = []
    for i in range(len(list_input)):
        if i % 2 == 0:
            new_list.insert(i, list_input[i+1])
        else:
            new_list.insert(i, list_input[i-1])
    print(new_list)
else:
    new_list = []
    for i in range(len(list_input)-1):
        if i % 2 == 0:
            new_list.insert(i, list_input[i+1])
        else:
            new_list.insert(i, list_input[i-1])
    new_list.insert(i+1, list_input[-1])
    print(new_list)



