name_city = 'Санкт-Петербург'
price = 88000
population = 4991000
print(f'Население города {name_city} {population} человек. Средняя стоимость квадратного метра жилья в городе {price} рублей.')

user_name_city = input('Введите название своего родного города: ')
user_population_city = int(input('Введите население своего родного города: '))

print(f'Название вашего родного города {user_name_city}. Его население {user_population_city} человек. '
      f'Разница с городом {name_city} составляет {abs(user_population_city - population)} человек')
