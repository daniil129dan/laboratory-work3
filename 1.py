def hypotenuse(leg1, leg2):
     return (leg1**2+leg2**2)**(0.5)
a = float(input('Введите длину первого катета: '))
b = float(input('Введите длину второго катета: '))

c = hypotenuse(a, b)

print('Длина гипотенузы: ', c)