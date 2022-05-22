def ChekPassword(a):
    b,c,d = 0, 0 ,0
    if (len(a)>=8):
        for i in range(len(a)):
            if a[i].isdigit():
                b +=1
            elif a[i].islower():
                c +=1
            elif a[i].isupper():
                d +=1
    if (b >=1)and(c >=1)and(d >=1):
        return True
    else:
        return False


#a = str(input('Введите пароль: ')) для упрвжнения 9
#print(ChekPassword(a))

