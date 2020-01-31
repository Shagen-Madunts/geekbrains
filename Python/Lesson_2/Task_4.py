"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_data = list(input('Введите несколько слов через пробел: ').split(' '))
work_list = [j for i in zip([j[:10] for j in user_data], [j[10:] for j in user_data]) for j in i if len(j) > 0]
fields = {x: y for x, y in zip(range(len(work_list)), work_list)}
for i, item in fields.items():
    print(f'{i}. {item}' if len(item) <= 10 else f'{i}. {item[:10]}\n{i}. {item[10:10+len(item)-10]}')
