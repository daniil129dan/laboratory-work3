def NextPrime(number):
    b = 0
    for i in range(1, number+1):
        if number % i == 0:
            b += 1
    if b == 2:
        print(number)
    else:
        number +=1
        NextPrime(number)

a = int(input('Введите число: '))

b = NextPrime(a+1)

