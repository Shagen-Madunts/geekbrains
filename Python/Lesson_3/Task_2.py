def user(name='Денис', surname='Иванов', born=1972,
         city='Москва', email='df@mail.ru', phone='+79182321212'):
    return print(f'Пользователь {name} по фамилии {surname} родился в {born} в городе {city}. '
                 f'Email: {email}, телефон {phone}')


user()
