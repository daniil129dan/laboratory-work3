BASE = 4.00
def taxy(distance):
    return (distance*0.25)/140

a = float(input('Введите расстояние поездки: '))

b = BASE+taxy(a)

print('Цена поездки: ', round(b,2),'$')