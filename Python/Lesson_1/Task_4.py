number = input('Введите число: ')
if len(number) >= 2:
    i = 0
    while i <= len(number)-1:
        if int(number[i]) >= int(number[i + 1]):
            larger_number = number[i]
        else:
            larger_number = number[i+1]
        i += 1
        print(larger_number)
else:
    print('Введите число а не цифру!')
    print('end program')
