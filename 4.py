def median(a,b,c):
    if (c>a>b) or (b>a>c):
        return a
    elif (a>b>c) or (c>b>a):
        return b
    else:
        return c

a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))

d = median(a,b,c)

print('Медиана трех чисел: ', d)