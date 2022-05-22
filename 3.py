def amount(am):
    if am == 1:
        return 10.95*am
    elif am > 1:
        return 10.95+2.95*(am - 1)


a = int(input('Введите количество позиций в заказе: '))

b = amount(a)

if b != None:
    print('Сумма доставки: ', b,'$')
else:
    print('Ошибка')



