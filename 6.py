def PrimeNumber(number):
    b = 0
    for i in range(1, number+1):
        if number % i == 0:
            b += 1
    if b == 2:
        return b==2
    else:
        return False
a = int(input('Введите число: '))

b = PrimeNumber(a)

print(b)