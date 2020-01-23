time_sec = int(input('Введите время в секундах: '))
if time_sec >= 0:
    hours = time_sec // 3600
    minutes = time_sec // 60
    seconds = time_sec % 60
    print('%02i:%02i:%02i' % (hours, minutes, seconds))
else:
    print('Введите положительное число!')
