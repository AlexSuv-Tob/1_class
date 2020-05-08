time = int(input('Введите время в секундах: '))

hour = time // 3600#вычисляем часы
minute = (time - (hour * 3600)) // 60#вычисляем минуты
sec = time - (hour * 3600 + minute * 60)#вычесляем секунды

print(f'Введенное время это {hour} часов : {minute} минут: {sec} секунд')